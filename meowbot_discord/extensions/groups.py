from discord import Member
from discord.ext import commands
from discord.ext.commands import Context, Bot, guild_only

from meowbot_discord.util import get_redis


@commands.group(
    invoke_without_command=True,
    name="groups",
    aliases=["group"],
    help="Ping group management",
)
@guild_only()
async def _groups(ctx: Context):
    await ctx.send_help(ctx.command)


@_groups.command(name="list", help="List all groups")
async def _groups_list(ctx: Context):
    redis = get_redis()
    guild_id = ctx.guild.id
    groups = redis.smembers(f"groups:{guild_id}")
    if len(groups) == 0:
        groups_str = "none"
    else:
        groups_str = ", ".join((f"`{group}`" for group in groups))
    await ctx.send(f"Groups on server: {groups_str}")


@_groups.command(name="create", help="Create a new group")
async def _groups_create(ctx: Context, name):
    redis = get_redis()
    guild_id = ctx.guild.id
    if redis.sismember(f"groups:{guild_id}", name):
        await ctx.send(f"Group `{name}` already exists!")
    else:
        redis.sadd(f"groups:{guild_id}", name)
        await ctx.send(f"Created group `{name}`!")


@_groups.command(name="add", help="Add members to a group")
async def _groups_add(ctx: Context, name, *members: Member):
    redis = get_redis()
    guild_id = ctx.guild.id
    if not redis.sismember(f"groups:{guild_id}", name):
        return await ctx.send(f"Group `{name}` doesn't exist!")
    if len(members) == 0:
        return await ctx.send("Must add at least 1 member")
    member_ids = (member.id for member in members)
    redis.sadd(f"groups:{guild_id}:{name}", *member_ids)
    members_str = ", ".join((member.mention for member in members))
    await ctx.send(f"Added {members_str} to `{name}`!")


@_groups.command(name="remove", help="Remove members from a group")
async def _groups_remove(ctx: Context, name, *members: Member):
    redis = get_redis()
    guild_id = ctx.guild.id
    if not redis.sismember(f"groups:{guild_id}", name):
        return await ctx.send(f"Group `{name}` doesn't exist!")
    if len(members) == 0:
        return await ctx.send("Must remove at least 1 member")
    member_ids = (member.id for member in members)
    redis.srem(f"groups:{guild_id}:{name}", *member_ids)
    members_str = ", ".join((member.mention for member in members))
    await ctx.send(f"Removed {members_str} from `{name}`!")


@_groups.command(name="delete", help="Delete a group")
async def _groups_delete(ctx: Context, name):
    redis = get_redis()
    guild_id = ctx.guild.id
    if not redis.sismember(f"groups:{guild_id}", name):
        return await ctx.send(f"Group `{name}` doesn't exist!")
    redis.srem(f"groups:{guild_id}", name)
    redis.delete(f"groups:{guild_id}:{name}")
    await ctx.send(f"Deleted group `{name}`!")


@_groups.command(name="ping", help="Ping a group")
async def _groups_ping(ctx: Context, name):
    redis = get_redis()
    guild_id = ctx.guild.id
    if not redis.sismember(f"groups:{guild_id}", name):
        return await ctx.send(f"Group `{name}` doesn't exist!")
    member_ids = redis.smembers(f"groups:{guild_id}:{name}")
    members = []
    for member_id in member_ids:
        member = ctx.guild.get_member(int(member_id))
        if member is not None:
            members.append(member)
    members_str = ", ".join((member.mention for member in members))
    await ctx.send(f"👆 {members_str}")


def setup(bot: Bot):
    bot.add_command(_groups)
