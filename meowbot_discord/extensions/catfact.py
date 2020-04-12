import requests
from discord.ext import commands
from discord.ext.commands import Context, Bot


@commands.command(name="fact", aliases=["catfact"], help="Get a cat fact")
async def _fact(ctx: Context):
    fact = requests.get("https://catfact.ninja/fact").json()["fact"]
    await ctx.send(fact)


def setup(bot: Bot):
    bot.add_command(_fact)
