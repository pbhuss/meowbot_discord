from discord.ext.commands import Context

from meowbot_discord.util import get_default_guild_id


class EmojiMap:
    def __init__(self, ctx: Context, guild_id=get_default_guild_id()):
        self._map = {
            emoji.name: emoji for emoji in ctx.bot.emojis if emoji.guild_id == guild_id
        }

    def __getattr__(self, item):
        if item in self._map:
            return self._map[item]
        raise AttributeError

    def __getitem__(self, item):
        return getattr(self, item)
