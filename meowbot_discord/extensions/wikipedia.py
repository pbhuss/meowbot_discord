from asyncio import sleep

from discord.ext import commands
from discord.ext.commands import Context, Bot, is_owner

from meowbot_discord.util import get_redis


WIKI_KEY = "wikipedia"


@commands.command(name="wikipedia", help="Play the Wikipedia game")
async def _wikipedia(ctx: Context):
    redis = get_redis()
    start, end = redis.srandmember(WIKI_KEY, number=2)
    prefix = "https://en.wikipedia.org/wiki/"
    await ctx.send("New game beginning in 5 seconds!")
    await sleep(5.0)
    await ctx.send(f"Ending article: {prefix}{end}")
    await ctx.send(f"You have 60 seconds to review the ending article")
    await sleep(60.0)
    await ctx.send(f"Starting article: {prefix}{start}")
    await ctx.send("Go!")


@commands.command(name="loadwiki", hidden=True)
@is_owner()
async def _load_wiki(ctx: Context, file):
    with open(file, "r") as fp:
        terms = list(fp)

    redis = get_redis()
    ct = 0
    for term in terms:
        term = term.strip()
        if term != "":
            redis.sadd(WIKI_KEY, term)
            ct += 1
    await ctx.send(f"Added {ct} phrases to wikipedia")


def setup(bot: Bot):
    bot.add_command(_wikipedia)
    bot.add_command(_load_wiki)
