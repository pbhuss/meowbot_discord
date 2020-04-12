import random

from discord.ext import commands
from discord.ext.commands import Context, Bot

from meowbot_discord.constants import magic_eight_ball_options


@commands.command(name="8ball", aliases=["magic8"], help="Ask meowbot a question")
async def _8ball(ctx: Context, *, question):
    text = "{} asked:\n> {}\n🎱 {}".format(
        ctx.message.author.mention, question, random.choice(magic_eight_ball_options),
    )
    await ctx.send(text)


def setup(bot: Bot):
    bot.add_command(_8ball)
