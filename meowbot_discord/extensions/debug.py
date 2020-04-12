import logging

from discord.ext import commands
from discord.ext.commands import Context, is_owner, Bot, ExtensionNotFound

from meowbot_discord.extensions import reload_all_extensions, load_or_reload_extension


@commands.command(name="ping", help="See if meowbot is awake")
async def _ping(ctx: Context):
    await ctx.send("🏓 pong!")


@commands.command(name="debug", hidden=True)
@is_owner()
async def _debug(ctx: Context):
    try:
        import ipdb
    except ImportError:
        await ctx.send("ipdb install not found")
    else:
        await ctx.send("entering debug mode")
        # reduce logging temporarily
        logging.basicConfig(level=logging.CRITICAL, force=True)
        ipdb.set_trace()
        logging.basicConfig(level=logging.INFO, force=True)


@commands.command(name="reload", help="Reloads all extensions", hidden=True)
@is_owner()
async def _reload(ctx: Context, *modules):
    if len(modules) == 0:
        reload_all_extensions(ctx.bot)
        await ctx.send("Reloaded all extensions")
    else:
        for module in modules:
            try:
                load_or_reload_extension(ctx.bot, module)
            except ExtensionNotFound:
                await ctx.send(f"Module `{module}` not found")
            else:
                await ctx.send(f"Reloaded `{module}`")


def setup(bot: Bot):
    bot.add_command(_ping)
    bot.add_command(_debug)
    bot.add_command(_reload)
