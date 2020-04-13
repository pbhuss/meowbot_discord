from discord.ext.commands import Bot, ExtensionAlreadyLoaded


DEFAULT_MODULES = ["8ball", "basic", "cat", "catfact", "debug", "groups", "xkcd"]


def load_all_extensions(bot: Bot):
    for module in DEFAULT_MODULES:
        bot.load_extension(f"{__name__}.{module}")


def reload_all_extensions(bot: Bot):
    for module in DEFAULT_MODULES:
        bot.reload_extension(f"{__name__}.{module}")


def load_or_reload_extension(bot: Bot, module: str):
    try:
        bot.load_extension(f"{__name__}.{module}")
    except ExtensionAlreadyLoaded:
        bot.reload_extension(f"{__name__}.{module}")
