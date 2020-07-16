#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:41:15 2020

@author: johnkylecooper
"""

import os
import time
from bot_utility import get_song_info

print('this is my twitter bot')

# Collect Keys
keys = open("keys.txt").read().split()

import twitter
api = twitter.Api(consumer_key=keys[0],
                  consumer_secret=keys[1],
                  access_token_key=keys[2],
                  access_token_secret=keys[3])

def tweet():
    song, lnk, year, H = get_song_info()
    file1 = open("songs.txt")
    past_songs = file1.read()
    file1.close()
    while song[H[1]] in past_songs:
        print('discovered repeat...')
        print('generating new song info...')
        song, lnk, year, H = get_song_info()
    status = 'Entering the Billboard Hot 100 top-ten singles on '\
                + song[H[0]] + ', ' + str(year) + ', "' + song[H[1]] + '" by '\
                + song[H[2]] + ' reached its peak on '\
                + song[H[4]] + ', ' + str(year) + '. ' + lnk
    print(status)
    # Write to a text file that lists the already posted songs
    file1 = open("songs.txt","a")
    file1.write(song[H[1]]+'\n')
    file1.close()
    api.PostUpdate(status)

tweet()