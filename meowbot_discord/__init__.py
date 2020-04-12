import logging

from meowbot_discord.bot import bot
from meowbot_discord.util import get_config
from meowbot_discord.commands import *  # noqa


def start_meowbot():
    logging.basicConfig(level=logging.INFO)
    config = get_config()
    bot.run(config["bot_token"])
