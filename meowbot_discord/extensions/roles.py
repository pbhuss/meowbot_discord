from discord import Member, RawReactionActionEvent, Emoji, Role, Guild
from discord.ext import commands
from discord.ext.commands import Context, Bot, guild_only, is_owner

from meowbot_discord.util import get_redis


REACTION_ADD = "REACTION_ADD"
REACTION_REMOVE = "REACTION_REMOVE"


class RoleManagement(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    async def _handle_reaction(self, payload: RawReactionActionEvent):
        redis = get_redis()
        key = f"role_mgmt:{payload.message_id}"
        if redis.exists(key):
            if int(redis.hget(key, "emoji_id")) == payload.emoji.id:
                role_id = int(redis.hget(key, "role_id"))
                guild = self.bot.get_guild(payload.guild_id)  # type: Guild
                member = guild.get_member(payload.user_id)  # type: Member
                role = guild.get_role(role_id)
                if payload.event_type == REACTION_ADD:
                    await member.add_roles(role, reason="via reaction")
                elif payload.event_type == REACTION_REMOVE:
                    await member.remove_roles(role, reason="via reaction")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: RawReactionActionEvent):
        await self._handle_reaction(payload)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: RawReactionActionEvent):
        await self._handle_reaction(payload)

    @commands.command(name="createrolemanagement")
    @guild_only()
    @is_owner()
    async def _create_role_management(self, ctx: Context, role: Role, emoji: Emoji):
        if not role.mentionable:
            return await ctx.send("Error: role is not mentionable")
        if not emoji.is_usable():
            return await ctx.send("Error: I can't use that emoji")
        message = await ctx.send(f"React with {emoji} to join {role.mention}")
        await message.add_reaction(emoji)
        redis = get_redis()
        key = f"role_mgmt:{message.id}"
        redis.hset(key, "emoji_id", emoji.id)
        redis.hset(key, "role_id", role.id)


def setup(bot: Bot):
    bot.add_cog(RoleManagement(bot))
