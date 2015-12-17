#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

# Checking if user has installed yaml on his machine
try:
    import yaml
except ImportError:
    print('[E] Yaml has not been installed or is not working')
    print('[H] Run "sudo pip3 install -r requirements.txt" from project root')
    exit(1)

def parse_config():
    '''
    Parses config
    returns dict(config)
    '''
    with open(os.path.join(os.path.expanduser('~'), '.rtcalarmrc'), 'r') as f:
        config = yaml.load(f.read())

    return config

def set_alarm(config):
    '''
    Sets alarm by executing bash command with rtcwake
    '''
    os.system([
        'sudo rtcwake -m {0} '.format(config['type']) + \
        '-u -t $(date -d "{0}" +%s) '.format(config['time']) + \
        '&& mplayer {0}'.format(config['music']) \
    ] [os.name=='nt'])

def check(config):
    '''
    Checks if all is ok
    exits if not
    '''
    # Allowed types of operation
    allowed_types = [
        'disk',
        'off',
        'no'
    ]

    # Checking if ~/.rtcalarmrc file exist
    if not os.path.isfile(config['music']):
        print('[E] Automatic tests failed')
        print('[R] Music file does not exist')
        exit(1)

    # Checking if type is allowed and valid
    elif config['type'] not in allowed_types:
        print('[E] Automatic tests failed')
        print('[R] Unknown type {0}'.format(config['type']))
        exit(1)


if __name__ == '__main__':
    # Checking if user sends some args
    if len(sys.argv) > 1:
        print('[E] Unrecognized args')
        print('[H] All configurations are performed in "~/.rtcalarmrc" file')
        exit(1)

    # Checking if ~/.rtcalarmrc file exist
    elif not os.path.isfile(os.path.join(os.path.expanduser('~'), '.rtcalarmrc')):
        print('[E] Config file not found')
        print('[H] Run "./init.py" from project root')
        exit(1)

    # Parsing config
    print('[I] Parsing config...')
    config = parse_config()
    print('[S] Parsed config\n')

    # Checking if all is ok
    print('[I] Checking entries...')
    check(config)
    print('[S] Automatic tests succeed\n')

    # Printing to user information from config
    print('[I*] Setting alarm for {0}'.format(config['time']))
    print('[I*] Using type {0}'.format(config['type']))
    print('[I*] Using music {0}'.format(config['music']))
    print('[Q] Are you agree? (y/n)')
    answer = input()

    if answer == 'y':
        print('\n')
        set_alarm(config)
    else:
        exit(0)
