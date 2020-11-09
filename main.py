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

bot = commands.Bot(command_prefix='!')


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
    user = ctx.author
    helpers.command_logger(user, 'TILTED')
    await basic_voice_command(user, 'audio/are-you-tilted.m4a')


@bot.command(name="ff", brief="landers saying can we please ff", pass_context=True)
async def on_ff(ctx):
    """
    Connects to voice channel and plays audio when !tilted command is used.
    Disconnects when audio is done playing.
    """
    user = ctx.author
    helpers.command_logger(user, 'FF')
    await basic_voice_command(user, 'audio/are-you-tilted.m4a')

bot.run(TOKEN)
