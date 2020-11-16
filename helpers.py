"""
basic helper functions
"""

import os
from datetime import datetime


def command_logger(user, command):
    """
    logs user and command at a certain time
    """
    print(f'{user} input {command} @ {datetime.now()}.')


def build_command_map(audio_dir):
    """
    Builds a dictionary based on the audio files in the audio folder
    """
    command_map = {}
    audio_files = os.listdir(audio_dir)
    for file in audio_files:
        command = file.split('.')[0]
        command_map[command] = file
    return command_map


def build_command_description(audio_dir):
    """
    Builds a command description based on the audio files in the audio folder
    """
    brief = ""
    audio_files = os.listdir(audio_dir)
    for file in audio_files:
        brief = brief + file.split('.')[0] + '\n'
    return brief
