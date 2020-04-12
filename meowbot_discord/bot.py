import logging

from discord.ext import commands


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    logging.info(f"We have logged in as {bot.user}")


@bot.event
async def on_disconnect():
    logging.info("Disconnected from Discord")
