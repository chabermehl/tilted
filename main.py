"""
This bot connects to discord and asks if you are tilted.
"""

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

import helpers

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
FFMPEG = os.getenv('FFMPEG')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    """
    Fires when bot has connected to discord.
    """
    print(f'{bot.user.name} has connected to Discord!')


async def basic_voice_command(user, sound_byte):
    """
    Plays a sound byte in whatever channel the user is in
    """
    if user.voice is not None:
        channel = user.voice.channel
        bot_voice = await channel.connect()
        bot_voice.play(discord.FFmpegPCMAudio(
            executable=FFMPEG, source=sound_byte))
        while bot_voice.is_playing():
            continue
        if not bot_voice.is_playing():
            await bot_voice.disconnect()
    else:
        print(f'{user} is not in voice chat.')


@bot.command(name="tilted", brief="plays an mp3 that asks Zaiah if hes tilted", pass_context=True)
async def on_tilted(ctx):
    """
    Connects to voice channel and plays audio when !tilted command is used.
    Disconnects when audio is done playing.
    """
    helpers.command_logger(ctx.author, 'TILTED')
    await basic_voice_command(ctx.author, 'audio/are-you-tilted.m4a')


@bot.command(name="dork", brief="Ya dork", pass_context=True)
async def on_stream(ctx):
    """
    ya dork??
    """
    helpers.command_logger(ctx.author, 'DORK')
    await basic_voice_command(ctx.author, 'audio/ya-dork.m4a')


@bot.command(name="ff", brief="landers saying can we please ff", pass_context=True)
async def on_ff(ctx):
    """
    Connects to voice channel and plays audio when !tilted command is used.
    Disconnects when audio is done playing.
    """
    helpers.command_logger(ctx.author, 'FF')
    await basic_voice_command(ctx.author, 'audio/FF.mp3')

# BEGIN: Fred based commands


@bot.command(name="unicef", brief="Fred on unicef mission", pass_context=True)
async def on_unicef(ctx):
    """
    Why donate when you can play league?
    """
    helpers.command_logger(ctx.author, 'UNICEF')
    await basic_voice_command(ctx.author, 'audio/unicef.mp3')


@bot.command(name="rolando", brief="head phone users beware", pass_context=True)
async def on_rolando(ctx):
    """
    No one asked for this
    """
    helpers.command_logger(ctx.author, 'ROLANDO')
    await basic_voice_command(ctx.author, 'audio/rolando.mp3')


@bot.command(name="bud", brief="Bud", pass_context=True)
async def on_bud(ctx):
    """
    Bud.
    """
    helpers.command_logger(ctx.author, 'BUD')
    await basic_voice_command(ctx.author, 'audio/YouGottaCutItOut.wav')

# END: Fred based commands


@bot.command(name="lose", brief="THE ONLY WAY TO LOSE IS TO NOT HAVE FUN", pass_context=True)
async def on_lose(ctx):
    """
    A signature Zaiah quote
    """
    helpers.command_logger(ctx.author, 'LOSE')
    await basic_voice_command(ctx.author, 'audio/only-way-to-lose.wav')


@bot.command(name="stream", brief="Wheres the stream?", pass_context=True)
async def on_stream(ctx):
    """
    Wheres the stream at tho?
    """
    helpers.command_logger(ctx.author, 'STREAM')
    await basic_voice_command(ctx.author, 'audio/stream.mp3')


@bot.command(name="idiotsinvoicechat", brief="the idiots", pass_context=True)
async def on_idiots(ctx):
    """
    Lists out all the idiots in chat
    """
    helpers.command_logger(ctx.author, 'IDIOTS')
    channel = ctx.message.guild.voice_channels[0]
    response = ''
    for mem in channel.members:
        response = response + \
            f'{mem.nick if mem.nick is not None else mem.name}\n'
    await ctx.send(response)


@bot.command(name="contribute", brief="Link to GitHub repo. Now accepting PRs")
async def on_contribute(ctx):
    """
    lets people know where the can contribute to the project at
    """
    helpers.command_logger(ctx.author, 'CONTRIBUTE')
    embed = discord.Embed(title="GitHub Repository", description="Now accepting PRs!",
                          url="https://github.com/chabermehl/titled")
    await ctx.send("https://github.com/chabermehl/tilted", embed=embed)

bot.run(TOKEN)
