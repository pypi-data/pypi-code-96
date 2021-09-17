import inspect

import pytest
from discord.ext import commands as dpy_commands

from redbot.core import commands


@pytest.fixture(scope="session")
def group():
    @commands.group()
    async def fixturegroup(*args, **kwargs):
        return args, kwargs

    return fixturegroup


def is_Command(obj):
    return isinstance(obj, commands.Command)


def is_Group(obj):
    return isinstance(obj, commands.Group)


def test_command_decorators(coroutine):
    assert is_Command(commands.command(name="cmd")(coroutine))
    assert is_Group(commands.group(name="grp")(coroutine))


def test_group_decorator_methods(group, coroutine):
    assert is_Command(group.command(name="cmd")(coroutine))
    assert is_Group(group.group(name="grp")(coroutine))


def test_bot_decorator_methods(red, coroutine):
    assert is_Command(red.command(name="cmd")(coroutine))
    assert is_Group(red.group(name="grp")(coroutine))


def test_dpy_commands_reexports():
    dpy_attrs = set()
    for attr_name, attr_value in dpy_commands.__dict__.items():
        if attr_name.startswith("_") or inspect.ismodule(attr_value):
            continue

        dpy_attrs.add(attr_name)

    missing_attrs = dpy_attrs - set(commands.__dict__.keys())

    assert not missing_attrs
