import requests
from discord.ext.commands import Context

from meowbot_discord.bot import bot


@bot.command(name="fact", aliases=["catfact"], help="Get a cat fact")
async def _fact(ctx: Context):
    fact = requests.get("https://catfact.ninja/fact").json()["fact"]
    await ctx.send(fact)
