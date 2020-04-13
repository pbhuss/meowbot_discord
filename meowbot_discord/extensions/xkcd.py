import datetime

import requests
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Bot


@commands.command(name="xkcd", help="Show today's XKCD (or a previous #)")
async def _xkcd(ctx: Context, number: int = None):
    if number is None:
        url = "http://xkcd.com/info.0.json"
    else:
        url = f"http://xkcd.com/{number}/info.0.json"

    resp = requests.get(url)
    if resp.status_code == 404:
        return await ctx.send("Comic not found")
    data = resp.json()

    title = f"#{data['num']}: {data['safe_title']}"
    dt = datetime.datetime(int(data["year"]), int(data["month"]), int(data["day"]))
    embed = Embed(title=title, description=data["alt"], timestamp=dt)
    embed.set_image(url=data["img"])
    await ctx.send(embed=embed)


def setup(bot: Bot):
    bot.add_command(_xkcd)
