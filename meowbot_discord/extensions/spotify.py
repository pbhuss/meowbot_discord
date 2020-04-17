from discord import Spotify, Embed
from discord.ext import commands
from discord.ext.commands import Context, Bot, guild_only


@commands.command(
    name="playing",
    aliases=["spotify", "nowplaying"],
    help="Share your currently playing song",
)
@guild_only()
async def _spotify(ctx: Context):
    spotify = None
    for activity in ctx.author.activities:
        if isinstance(activity, Spotify):
            spotify = activity

    if spotify is None:
        return await ctx.send(
            "Nothing currently playing (make sure your Spotify is linked)"
        )
    else:
        embed = Embed(
            title=f"{spotify.artist} - {spotify.title}",
            description=spotify.album,
            color=spotify.colour,
            url=f"https://open.spotify.com/track/{spotify.track_id}",
        )
        embed.set_image(url=spotify.album_cover_url)
        return await ctx.send(
            content=f"{ctx.author.mention} is listening to:", embed=embed
        )


def setup(bot: Bot):
    bot.add_command(_spotify)
