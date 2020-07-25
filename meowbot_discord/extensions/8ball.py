import random
import re

from discord.ext import commands
from discord.ext.commands import Context, Bot

from meowbot_discord.constants import magic_eight_ball_options


@commands.command(name="8ball", aliases=["magic8"], help="Ask meowbot a question")
async def _8ball(ctx: Context, *, question):
    text = "{} asked:\n> {}\n🎱 {}".format(
        ctx.message.author.mention, question, random.choice(magic_eight_ball_options),
    )
    await ctx.send(text)


@commands.command(name="roll", help="Roll some dice")
async def _roll(ctx: Context, *, roll):
    result = re.search(r"(\d+)d(\d+)", roll)
    if result is None:
        await ctx.send("Usage: `!roll {x}d{y}`")
        return

    num_dice = int(result.group(1))
    num_sides = int(result.group(2))
    if num_dice > 100 or num_sides < 2:
        await ctx.send("No.")
        return
    rolls = (random.randint(1, num_sides) for _ in range(num_dice))
    await ctx.send(f"🎲 I rolled: {', '.join(map(str, rolls))}")


def setup(bot: Bot):
    bot.add_command(_8ball)
    bot.add_command(_roll)
