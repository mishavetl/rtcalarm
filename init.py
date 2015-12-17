#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

def create_config():
    """
    Creates init config file
    """
    # Builtin Music Directory
    builtin_music = os.path.join(os.path.dirname(os.path.abspath(__file__)), \
        'builtin_music', 'greenday-basketcase.mp3')

    with open(os.path.join(os.path.expanduser('~'), '.rtcalarmrc'), 'w+') as f:
        f.write('''## RTC Alarm Config File

# NOTE! You can set only one alarm, type and music a time

# Types:
# disk - save session to disk and shutdown
# no   - dont shutdown now but save data about starting up
# off  - shutdown now and dont save session

## Alarms
# time: 5:30 am
# time: 5:40 am
time: tomorrow 7:00 am

## Types
# type: 'off'
# type: 'no'
type: disk

## Music
music: {0}'''.format(builtin_music))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print('[E] Unrecognized args')
        print('[H] This script dont gets any args')
        exit(1)

    if os.path.isfile('~/.rtcalarmrc'):
        print('[E] ~/.rtcalarmrc already exists')
        print('[H] Try deleting it')
        exit(1)

    create_config()
