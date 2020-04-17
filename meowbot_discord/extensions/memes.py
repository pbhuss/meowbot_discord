import frogtips.api
import requests
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Bot


@commands.command(name="inspire", help="Get inspired")
async def _inspire(ctx: Context):
    embed = Embed()
    embed.set_image(url=requests.get("https://inspirobot.me/api?generate=true").text)
    return await ctx.send(embed=embed)


@commands.command(name="tip", aliases=["frogtip"], help="Get a frog tip")
async def _tip(ctx: Context):
    frog_tip = frogtips.api.Tips().get_next_tip()
    return await ctx.send(f"🐸 {frog_tip.tip}")


def setup(bot: Bot):
    bot.add_command(_inspire)
    bot.add_command(_tip)
