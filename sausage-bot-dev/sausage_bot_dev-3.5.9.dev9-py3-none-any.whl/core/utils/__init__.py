from __future__ import annotations
import asyncio
import json
import logging
from asyncio import as_completed, Semaphore
from asyncio.futures import isfuture
from itertools import chain
from pathlib import Path
from typing import (
    Any,
    AsyncIterator,
    AsyncIterable,
    Awaitable,
    Callable,
    Iterable,
    Iterator,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
    Generator,
    Coroutine,
)

from discord.utils import maybe_coroutine

__all__ = (
    "bounded_gather",
    "bounded_gather_iter",
    "deduplicate_iterables",
    "AsyncIter",
    "get_end_user_data_statement",
    "get_end_user_data_statement_or_raise",
)

log = logging.getLogger("red.core.utils")

_T = TypeVar("_T")
_S = TypeVar("_S")

# Benchmarked to be the fastest method.
def deduplicate_iterables(*iterables):
    """
    Returns a list of all unique items in ``iterables``, in the order they
    were first encountered.
    """
    # dict insertion order is guaranteed to be preserved in 3.6+
    return list(dict.fromkeys(chain.from_iterable(iterables)))


# https://github.com/PyCQA/pylint/issues/2717
class AsyncFilter(AsyncIterator[_T], Awaitable[List[_T]]):  # pylint: disable=duplicate-bases
    """Class returned by `async_filter`. See that function for details.

    We don't recommend instantiating this class directly.
    """

    def __init__(
        self,
        func: Callable[[_T], Union[bool, Awaitable[bool]]],
        iterable: Union[AsyncIterable[_T], Iterable[_T]],
    ) -> None:
        self.__func: Callable[[_T], Union[bool, Awaitable[bool]]] = func
        self.__iterable: Union[AsyncIterable[_T], Iterable[_T]] = iterable

        # We assign the generator strategy based on the arguments' types
        if isinstance(iterable, AsyncIterable):
            if asyncio.iscoroutinefunction(func):
                self.__generator_instance = self.__async_generator_async_pred()
            else:
                self.__generator_instance = self.__async_generator_sync_pred()
        elif asyncio.iscoroutinefunction(func):
            self.__generator_instance = self.__sync_generator_async_pred()
        else:
            raise TypeError("Must be either an async predicate, an async iterable, or both.")

    async def __sync_generator_async_pred(self) -> AsyncIterator[_T]:
        for item in self.__iterable:
            if await self.__func(item):
                yield item

    async def __async_generator_sync_pred(self) -> AsyncIterator[_T]:
        async for item in self.__iterable:
            if self.__func(item):
                yield item

    async def __async_generator_async_pred(self) -> AsyncIterator[_T]:
        async for item in self.__iterable:
            if await self.__func(item):
                yield item

    async def __flatten(self) -> List[_T]:
        return [item async for item in self]

    def __aiter__(self):
        return self

    def __await__(self):
        # Simply return the generator filled into a list
        return self.__flatten().__await__()

    def __anext__(self) -> Awaitable[_T]:
        # This will use the generator strategy set in __init__
        return self.__generator_instance.__anext__()


def async_filter(
    func: Callable[[_T], Union[bool, Awaitable[bool]]],
    iterable: Union[AsyncIterable[_T], Iterable[_T]],
) -> AsyncFilter[_T]:
    """Filter an (optionally async) iterable with an (optionally async) predicate.

    At least one of the arguments must be async.

    Parameters
    ----------
    func : Callable[[T], Union[bool, Awaitable[bool]]]
        A function or coroutine function which takes one item of ``iterable``
        as an argument, and returns ``True`` or ``False``.
    iterable : Union[AsyncIterable[_T], Iterable[_T]]
        An iterable or async iterable which is to be filtered.

    Raises
    ------
    TypeError
        If neither of the arguments are async.

    Returns
    -------
    AsyncFilter[T]
        An object which can either be awaited to yield a list of the filtered
        items, or can also act as an async iterator to yield items one by one.

    """
    return AsyncFilter(func, iterable)


async def async_enumerate(
    async_iterable: AsyncIterable[_T], start: int = 0
) -> AsyncIterator[Tuple[int, _T]]:
    """Async iterable version of `enumerate`.

    Parameters
    ----------
    async_iterable : AsyncIterable[T]
        The iterable to enumerate.
    start : int
        The index to start from. Defaults to 0.

    Returns
    -------
    AsyncIterator[Tuple[int, T]]
        An async iterator of tuples in the form of ``(index, item)``.

    """
    async for item in async_iterable:
        yield start, item
        start += 1


async def _sem_wrapper(sem, task):
    async with sem:
        return await task


def bounded_gather_iter(
    *coros_or_futures, limit: int = 4, semaphore: Optional[Semaphore] = None
) -> Iterator[Awaitable[Any]]:
    """
    An iterator that returns tasks as they are ready, but limits the
    number of tasks running at a time.

    Parameters
    ----------
    *coros_or_futures
        The awaitables to run in a bounded concurrent fashion.
    limit : Optional[`int`]
        The maximum number of concurrent tasks. Used when no ``semaphore``
        is passed.
    semaphore : Optional[:class:`asyncio.Semaphore`]
        The semaphore to use for bounding tasks. If `None`, create one
        using ``loop`` and ``limit``.

    Raises
    ------
    TypeError
        When invalid parameters are passed
    """
    loop = asyncio.get_running_loop()

    if semaphore is None:
        if not isinstance(limit, int) or limit <= 0:
            raise TypeError("limit must be an int > 0")

        semaphore = Semaphore(limit)

    pending = []

    for cof in coros_or_futures:
        if isfuture(cof) and cof._loop is not loop:
            raise ValueError("futures are tied to different event loops")

        cof = _sem_wrapper(semaphore, cof)
        pending.append(cof)

    return as_completed(pending)


def bounded_gather(
    *coros_or_futures,
    return_exceptions: bool = False,
    limit: int = 4,
    semaphore: Optional[Semaphore] = None,
) -> Awaitable[List[Any]]:
    """
    A semaphore-bounded wrapper to :meth:`asyncio.gather`.

    Parameters
    ----------
    *coros_or_futures
        The awaitables to run in a bounded concurrent fashion.
    return_exceptions : bool
        If true, gather exceptions in the result list instead of raising.
    limit : Optional[`int`]
        The maximum number of concurrent tasks. Used when no ``semaphore``
        is passed.
    semaphore : Optional[:class:`asyncio.Semaphore`]
        The semaphore to use for bounding tasks. If `None`, create one
        using ``loop`` and ``limit``.

    Raises
    ------
    TypeError
        When invalid parameters are passed
    """
    loop = asyncio.get_running_loop()

    if semaphore is None:
        if not isinstance(limit, int) or limit <= 0:
            raise TypeError("limit must be an int > 0")

        semaphore = Semaphore(limit)

    tasks = (_sem_wrapper(semaphore, task) for task in coros_or_futures)

    return asyncio.gather(*tasks, return_exceptions=return_exceptions)


class AsyncIter(AsyncIterator[_T], Awaitable[List[_T]]):  # pylint: disable=duplicate-bases
    """Asynchronous iterator yielding items from ``iterable``
    that sleeps for ``delay`` seconds every ``steps`` items.

    Parameters
    ----------
    iterable: Iterable
        The iterable to make async.
    delay: Union[float, int]
        The amount of time in seconds to sleep.
    steps: int
        The number of iterations between sleeps.

    Raises
    ------
    ValueError
        When ``steps`` is lower than 1.

    Examples
    --------
    >>> from redbot.core.utils import AsyncIter
    >>> async for value in AsyncIter(range(3)):
    ...     print(value)
    0
    1
    2

    """

    def __init__(
        self, iterable: Iterable[_T], delay: Union[float, int] = 0, steps: int = 1
    ) -> None:
        if steps < 1:
            raise ValueError("Steps must be higher than or equals to 1")
        self._delay = delay
        self._iterator = iter(iterable)
        self._i = 0
        self._steps = steps
        self._map = None

    def __aiter__(self) -> AsyncIter[_T]:
        return self

    async def __anext__(self) -> _T:
        try:
            item = next(self._iterator)
        except StopIteration:
            raise StopAsyncIteration
        if self._i == self._steps:
            self._i = 0
            await asyncio.sleep(self._delay)
        self._i += 1
        return await maybe_coroutine(self._map, item) if self._map is not None else item

    def __await__(self) -> Generator[Any, None, List[_T]]:
        """Returns a list of the iterable.

        Examples
        --------
        >>> from redbot.core.utils import AsyncIter
        >>> iterator = AsyncIter(range(5))
        >>> await iterator
        [0, 1, 2, 3, 4]

        """
        return self.flatten().__await__()

    async def next(self, default: Any = ...) -> _T:
        """Returns a next entry of the iterable.

        Parameters
        ----------
        default: Optional[Any]
            The value to return if the iterator is exhausted.

        Raises
        ------
        StopAsyncIteration
            When ``default`` is not specified and the iterator has been exhausted.

        Examples
        --------
        >>> from redbot.core.utils import AsyncIter
        >>> iterator = AsyncIter(range(5))
        >>> await iterator.next()
        0
        >>> await iterator.next()
        1

        """
        try:
            value = await self.__anext__()
        except StopAsyncIteration:
            if default is ...:
                raise
            value = default
        return value

    async def flatten(self) -> List[_T]:
        """Returns a list of the iterable.

        Examples
        --------
        >>> from redbot.core.utils import AsyncIter
        >>> iterator = AsyncIter(range(5))
        >>> await iterator.flatten()
        [0, 1, 2, 3, 4]

        """
        return [item async for item in self]

    def filter(self, function: Callable[[_T], Union[bool, Awaitable[bool]]]) -> AsyncFilter[_T]:
        """Filter the iterable with an (optionally async) predicate.

        Parameters
        ----------
        function: Callable[[T], Union[bool, Awaitable[bool]]]
            A function or coroutine function which takes one item of ``iterable``
            as an argument, and returns ``True`` or ``False``.

        Returns
        -------
        AsyncFilter[T]
            An object which can either be awaited to yield a list of the filtered
            items, or can also act as an async iterator to yield items one by one.

        Examples
        --------
        >>> from redbot.core.utils import AsyncIter
        >>> def predicate(value):
        ...     return value <= 5
        >>> iterator = AsyncIter([1, 10, 5, 100])
        >>> async for i in iterator.filter(predicate):
        ...     print(i)
        1
        5

        >>> from redbot.core.utils import AsyncIter
        >>> def predicate(value):
        ...     return value <= 5
        >>> iterator = AsyncIter([1, 10, 5, 100])
        >>> await iterator.filter(predicate)
        [1, 5]

        """
        return async_filter(function, self)

    def enumerate(self, start: int = 0) -> AsyncIterator[Tuple[int, _T]]:
        """Async iterable version of `enumerate`.

        Parameters
        ----------
        start: int
            The index to start from. Defaults to 0.

        Returns
        -------
        AsyncIterator[Tuple[int, T]]
            An async iterator of tuples in the form of ``(index, item)``.

        Examples
        --------
        >>> from redbot.core.utils import AsyncIter
        >>> iterator = AsyncIter(['one', 'two', 'three'])
        >>> async for i in iterator.enumerate(start=10):
        ...     print(i)
        (10, 'one')
        (11, 'two')
        (12, 'three')

        """
        return async_enumerate(self, start)

    async def without_duplicates(self) -> AsyncIterator[_T]:
        """
        Iterates while omitting duplicated entries.

        Examples
        --------
        >>> from redbot.core.utils import AsyncIter
        >>> iterator = AsyncIter([1,2,3,3,4,4,5])
        >>> async for i in iterator.without_duplicates():
        ...     print(i)
        1
        2
        3
        4
        5

        """
        _temp = set()
        async for item in self:
            if item not in _temp:
                yield item
                _temp.add(item)
        del _temp

    async def find(
        self,
        predicate: Callable[[_T], Union[bool, Awaitable[bool]]],
        default: Optional[Any] = None,
    ) -> AsyncIterator[_T]:
        """Calls ``predicate`` over items in iterable and return first value to match.

        Parameters
        ----------
        predicate: Union[Callable, Coroutine]
            A function that returns a boolean-like result. The predicate provided can be a coroutine.
        default: Optional[Any]
            The value to return if there are no matches.

        Raises
        ------
        TypeError
            When ``predicate`` is not a callable.

        Examples
        --------
        >>> from redbot.core.utils import AsyncIter
        >>> await AsyncIter(range(3)).find(lambda x: x == 1)
        1
        """
        while True:
            try:
                elem = await self.__anext__()
            except StopAsyncIteration:
                return default
            ret = await maybe_coroutine(predicate, elem)
            if ret:
                return elem

    def map(self, func: Callable[[_T], Union[_S, Awaitable[_S]]]) -> AsyncIter[_S]:
        """Set the mapping callable for this instance of `AsyncIter`.

        .. important::
            This should be called after AsyncIter initialization and before any other of its methods.

        Parameters
        ----------
        func: Union[Callable, Coroutine]
            The function to map values to. The function provided can be a coroutine.

        Raises
        ------
        TypeError
            When ``func`` is not a callable.

        Examples
        --------
        >>> from redbot.core.utils import AsyncIter
        >>> async for value in AsyncIter(range(3)).map(bool):
        ...     print(value)
        False
        True
        True

        """

        if not callable(func):
            raise TypeError("Mapping must be a callable.")
        self._map = func
        return self


def get_end_user_data_statement(file: Union[Path, str]) -> Optional[str]:
    """
    This function attempts to get the ``end_user_data_statement`` key from cog's ``info.json``.
    This will log the reason if ``None`` is returned.

    Parameters
    ----------
    file: Union[pathlib.Path, str]
        The ``__file__`` variable for the cog's ``__init__.py`` file.

    Returns
    -------
    Optional[str]
        The end user data statement found in the info.json
        or ``None`` if there was an issue finding one.

    Examples
    --------
    >>> # In cog's `__init__.py`
    >>> from redbot.core.utils import get_end_user_data_statement
    >>> __red_end_user_data_statement__  = get_end_user_data_statement(__file__)
    >>> def setup(bot):
    ...     ...
    """
    try:
        file = Path(file).parent.absolute()
        info_json = file / "info.json"
        statement = get_end_user_data_statement_or_raise(info_json)
    except FileNotFoundError:
        log.critical("'%s' does not exist.", str(info_json))
    except KeyError:
        log.critical("'%s' is missing an entry for 'end_user_data_statement'", str(info_json))
    except json.JSONDecodeError as exc:
        log.critical("'%s' is not a valid JSON file.", str(info_json), exc_info=exc)
    except UnicodeError as exc:
        log.critical("'%s' has a bad encoding.", str(info_json), exc_info=exc)
    except Exception as exc:
        log.critical(
            "There was an error when trying to load the end user data statement from '%s'.",
            str(info_json),
            exc_info=exc,
        )
    else:
        return statement
    return None


def get_end_user_data_statement_or_raise(file: Union[Path, str]) -> str:
    """
    This function attempts to get the ``end_user_data_statement`` key from cog's ``info.json``.

    Parameters
    ----------
    file: Union[pathlib.Path, str]
        The ``__file__`` variable for the cog's ``__init__.py`` file.

    Returns
    -------
    str
        The end user data statement found in the info.json.

    Raises
    ------
    FileNotFoundError
        When ``info.json`` does not exist.
    KeyError
        When ``info.json`` does not have the ``end_user_data_statement`` key.
    json.JSONDecodeError
        When ``info.json`` can't be decoded with ``json.load()``
    UnicodeError
        When ``info.json`` can't be decoded due to bad encoding.
    Exception
        Any other exception raised from ``pathlib`` and ``json`` modules
        when attempting to parse the ``info.json`` for the ``end_user_data_statement`` key.
    """
    file = Path(file).parent.absolute()
    info_json = file / "info.json"
    with info_json.open(encoding="utf-8") as fp:
        return json.load(fp)["end_user_data_statement"]
