"""
This bot connects to discord and asks if you are tilted.
"""

import os
from datetime import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
FFMPEG = os.getenv('FFMPEG')
AUDIO_SOURCE = os.getenv('AUDIO_SOURCE')

bot = commands.Bot(command_prefix='!')


# FFMPEG = """C:/Users/charles/Documents/ffmpeg-20200831-4a11a6f-win64-static/ffmpeg-20200831-4a11a6f-win64-static/bin/ffmpeg.exe"""
# AUDIO_SOURCE = "are-you-tilted.m4a"


@bot.event
async def on_ready():
    """
    Fires when bot has connected to discord.
    """
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="tilted", brief="plays an mp3 that asks Zaiah if hes tilted", pass_context=True)
async def on_tilted(ctx):
    """
    Connects to voice channel and plays audio when !tilted command is used. 
    Disconnects when audio is done playing. 
    """
    user = ctx.author
    print(f'{user} input command TILTED @ {datetime.now()}.')
    if user.voice is not None:
        channel = user.voice.channel
        bot_voice = await channel.connect()
        bot_voice.play(discord.FFmpegPCMAudio(
            executable=FFMPEG, source=AUDIO_SOURCE))
        while bot_voice.is_playing():
            print('playing...')
        if not bot_voice.is_playing():
            await bot_voice.disconnect()

bot.run(TOKEN)
