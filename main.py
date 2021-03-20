import os
import discord
from discord.ext import commands
from fpl import get_fixture, HELLO, SHORT_TEAMS, get_team_fixture
from scorecard import get_score
from standings import get_table

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print(f"Bot ready")


@client.command()
async def hello(ctx):
    await ctx.send(HELLO)


@client.command()
async def gwFixture(ctx, gw: int = None):
    if gw:
        await ctx.send(f"```{get_fixture(gw)}```")
    else:
        await ctx.send(f"```{get_fixture()}```")


@client.command()
async def teamFixture(ctx, team: str, gw: int = 5):
    await ctx.send("\n".join(get_team_fixture(team, gw)))


@client.command()
async def getTeams(ctx):
    teams = "\n".join(SHORT_TEAMS.values())

    await ctx.send(teams)


@client.command()
async def getTable(ctx):

    await ctx.send(f"```{get_table()}```")


@client.command()
async def liveScore(ctx, *, arg):
    try:
        await ctx.send(get_score(arg))
    except:
        await ctx.send(f"No match in progress for {arg}")


client.run(os.environ.get('DISCORD_TOKEN'))
