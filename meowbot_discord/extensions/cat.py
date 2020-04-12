import requests
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Bot

from meowbot_discord.util import get_cat_api_key


@commands.command(name="cat", help="Gives one cat")
async def _cat(ctx: Context):
    image_url = requests.head(
        "https://api.thecatapi.com/v1/images/search?format=src&mime_types=image/gif",
        headers={"x-api-key": get_cat_api_key()},
    ).headers["Location"]
    embed = Embed()
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)


def setup(bot: Bot):
    bot.add_command(_cat)
