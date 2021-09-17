########## SENSITIVE SECTION WARNING ###########
################################################
# Any edits of any of the exported names       #
# may result in a breaking change.             #
# Ensure no names are removed without warning. #
################################################

from .commands import (
    Cog as Cog,
    CogMixin as CogMixin,
    CogCommandMixin as CogCommandMixin,
    CogGroupMixin as CogGroupMixin,
    Command as Command,
    Group as Group,
    GroupMixin as GroupMixin,
    command as command,
    group as group,
    RedUnhandledAPI as RedUnhandledAPI,
    RESERVED_COMMAND_NAMES as RESERVED_COMMAND_NAMES,
)
from .context import Context as Context, GuildContext as GuildContext, DMContext as DMContext
from .converter import (
    DictConverter as DictConverter,
    TimedeltaConverter as TimedeltaConverter,
    get_dict_converter as get_dict_converter,
    get_timedelta_converter as get_timedelta_converter,
    parse_timedelta as parse_timedelta,
    NoParseOptional as NoParseOptional,
    UserInputOptional as UserInputOptional,
    Literal as Literal,
)
from .errors import (
    ConversionFailure as ConversionFailure,
    BotMissingPermissions as BotMissingPermissions,
    UserFeedbackCheckFailure as UserFeedbackCheckFailure,
    ArgParserFailure as ArgParserFailure,
)
from .help import (
    red_help as red_help,
    RedHelpFormatter as RedHelpFormatter,
    HelpSettings as HelpSettings,
)
from .requires import (
    CheckPredicate as CheckPredicate,
    DM_PERMS as DM_PERMS,
    GlobalPermissionModel as GlobalPermissionModel,
    GuildPermissionModel as GuildPermissionModel,
    PermissionModel as PermissionModel,
    PrivilegeLevel as PrivilegeLevel,
    PermState as PermState,
    Requires as Requires,
    permissions_check as permissions_check,
    bot_has_permissions as bot_has_permissions,
    bot_in_a_guild as bot_in_a_guild,
    has_permissions as has_permissions,
    has_guild_permissions as has_guild_permissions,
    is_owner as is_owner,
    guildowner as guildowner,
    guildowner_or_permissions as guildowner_or_permissions,
    admin as admin,
    admin_or_permissions as admin_or_permissions,
    mod as mod,
    mod_or_permissions as mod_or_permissions,
)

from ._dpy_reimplements import (
    check as check,
    guild_only as guild_only,
    cooldown as cooldown,
    dm_only as dm_only,
    is_nsfw as is_nsfw,
    has_role as has_role,
    has_any_role as has_any_role,
    bot_has_role as bot_has_role,
    when_mentioned_or as when_mentioned_or,
    when_mentioned as when_mentioned,
    bot_has_any_role as bot_has_any_role,
    before_invoke as before_invoke,
    after_invoke as after_invoke,
)

### DEP-WARN: Check this *every* discord.py update
from discord.ext.commands import (
    BadArgument as BadArgument,
    EmojiConverter as EmojiConverter,
    GuildConverter as GuildConverter,
    InvalidEndOfQuotedStringError as InvalidEndOfQuotedStringError,
    MemberConverter as MemberConverter,
    BotMissingRole as BotMissingRole,
    PrivateMessageOnly as PrivateMessageOnly,
    HelpCommand as HelpCommand,
    MinimalHelpCommand as MinimalHelpCommand,
    DisabledCommand as DisabledCommand,
    ExtensionFailed as ExtensionFailed,
    Bot as Bot,
    NotOwner as NotOwner,
    CategoryChannelConverter as CategoryChannelConverter,
    CogMeta as CogMeta,
    ConversionError as ConversionError,
    UserInputError as UserInputError,
    Converter as Converter,
    InviteConverter as InviteConverter,
    ExtensionError as ExtensionError,
    Cooldown as Cooldown,
    CheckFailure as CheckFailure,
    PartialMessageConverter as PartialMessageConverter,
    MessageConverter as MessageConverter,
    MissingPermissions as MissingPermissions,
    BadUnionArgument as BadUnionArgument,
    DefaultHelpCommand as DefaultHelpCommand,
    ExtensionNotFound as ExtensionNotFound,
    UserConverter as UserConverter,
    MissingRole as MissingRole,
    CommandOnCooldown as CommandOnCooldown,
    MissingAnyRole as MissingAnyRole,
    ExtensionNotLoaded as ExtensionNotLoaded,
    clean_content as clean_content,
    CooldownMapping as CooldownMapping,
    ArgumentParsingError as ArgumentParsingError,
    RoleConverter as RoleConverter,
    CommandError as CommandError,
    TextChannelConverter as TextChannelConverter,
    UnexpectedQuoteError as UnexpectedQuoteError,
    Paginator as Paginator,
    BucketType as BucketType,
    NoEntryPointError as NoEntryPointError,
    CommandInvokeError as CommandInvokeError,
    TooManyArguments as TooManyArguments,
    Greedy as Greedy,
    ExpectedClosingQuoteError as ExpectedClosingQuoteError,
    ColourConverter as ColourConverter,
    ColorConverter as ColorConverter,
    VoiceChannelConverter as VoiceChannelConverter,
    StageChannelConverter as StageChannelConverter,
    StoreChannelConverter as StoreChannelConverter,
    NSFWChannelRequired as NSFWChannelRequired,
    IDConverter as IDConverter,
    MissingRequiredArgument as MissingRequiredArgument,
    GameConverter as GameConverter,
    CommandNotFound as CommandNotFound,
    BotMissingAnyRole as BotMissingAnyRole,
    NoPrivateMessage as NoPrivateMessage,
    AutoShardedBot as AutoShardedBot,
    ExtensionAlreadyLoaded as ExtensionAlreadyLoaded,
    PartialEmojiConverter as PartialEmojiConverter,
    check_any as check_any,
    max_concurrency as max_concurrency,
    CheckAnyFailure as CheckAnyFailure,
    MaxConcurrency as MaxConcurrency,
    MaxConcurrencyReached as MaxConcurrencyReached,
    bot_has_guild_permissions as bot_has_guild_permissions,
    CommandRegistrationError as CommandRegistrationError,
    GuildNotFound as GuildNotFound,
    MessageNotFound as MessageNotFound,
    MemberNotFound as MemberNotFound,
    UserNotFound as UserNotFound,
    ChannelNotFound as ChannelNotFound,
    ChannelNotReadable as ChannelNotReadable,
    BadColourArgument as BadColourArgument,
    RoleNotFound as RoleNotFound,
    BadInviteArgument as BadInviteArgument,
    EmojiNotFound as EmojiNotFound,
    PartialEmojiConversionFailure as PartialEmojiConversionFailure,
    BadBoolArgument as BadBoolArgument,
)
