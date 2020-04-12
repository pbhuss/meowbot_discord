import logging

from meowbot_discord.bot import bot
from meowbot_discord.extensions import load_all_extensions
from meowbot_discord.util import get_config


def start_meowbot():
    logging.basicConfig(level=logging.INFO)
    config = get_config()
    load_all_extensions(bot)
    bot.run(config["bot_token"])
