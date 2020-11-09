"""
basic helper functions
"""

from datetime import datetime


def command_logger(user, command):
    """
    logs user and command at a certain time
    """
    print(f'{user} input {command} @ {datetime.now()}.')
