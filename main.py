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


@bot.command(name="tilt", brief="an assortment of potentially tilting commands", description=helpers.build_command_description('audio'), pass_context=True)
async def on_tilt(ctx, command: str):
    """
    Handles the tilt command and its various options
    """
    helpers.command_logger(ctx.author, f'TILT {command}')
    command_map = helpers.build_command_map('audio')
    await basic_voice_command(ctx.author, f'audio/{command_map[command]}')


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
