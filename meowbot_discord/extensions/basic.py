import random

from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Bot

from meowbot_discord.emoji import EmojiMap


@commands.command(
    name="shrug", help="Shrug",
)
async def _shrug(ctx: Context):
    await ctx.send(rf"`¯\_🐱_/¯`")


@commands.command(
    name="meow", help="Meow!",
)
async def _meow(ctx: Context):
    emoji = EmojiMap(ctx)
    await ctx.send(f"Meow! {emoji.catkool}")


@commands.command(
    name="no", aliases=["bad", "stop"], help="Bad kitty!",
)
async def _no(ctx: Context):
    options = [
        "https://media.giphy.com/media/mYbsoApPfp0cg/giphy.gif",
        "https://media.giphy.com/media/dXO1Cy51pMrGU/giphy.gif",
        "https://media.giphy.com/media/ZXWZ6q1HYYpR6/giphy.gif",
        "https://media.giphy.com/media/kpMRmXUtsOeIg/giphy.gif",
        "https://media.giphy.com/media/xg0nPTCKIPJRe/giphy.gif",
    ]
    embed = Embed()
    embed.set_image(url=random.choice(options))
    await ctx.send(embed=embed)


@commands.command(
    name="high5", aliases=["highfive", "hi5"], help="Give meowbot a high five",
)
async def _high5(ctx: Context):
    embed = Embed()
    embed.set_image(url="https://media.giphy.com/media/10ZEx0FoCU2XVm/giphy.gif")
    await ctx.send(embed=embed)


@commands.command(
    name="choose",
    aliases=["choice"],
    help="Choose from multiple options (comma-separated)",
)
async def _choose(ctx: Context, *, arg):
    result = random.choice(arg.split(",")).strip()
    await ctx.send(f"{ctx.message.author.mention}: {result}")


@commands.command(
    name="catnip", help="Give meowbot some catnip",
)
async def _catnip(ctx: Context):
    embed = Embed(description="Oh no! You gave meowbot catnip 🌿")
    embed.set_image(url="https://media.giphy.com/media/DX6y0ENWjEGPe/giphy.gif")
    await ctx.send(embed=embed)


@commands.command(name="nyan",)
async def _nyan(ctx: Context):
    embed = Embed()
    embed.set_image(url="https://media.giphy.com/media/sIIhZliB2McAo/giphy.gif")
    await ctx.send(embed=embed)


def setup(bot: Bot):
    bot.add_command(_shrug)
    bot.add_command(_meow)
    bot.add_command(_no)
    bot.add_command(_high5)
    bot.add_command(_choose)
    bot.add_command(_catnip)
    bot.add_command(_nyan)
