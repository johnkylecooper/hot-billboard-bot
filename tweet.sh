#!/bin/bash

source ~/opt/anaconda3/etc/profile.d/conda.sh
source keys.env

conda activate base

# Retry up to 10 times
for _ in {1..10}; do
python my_twitter_bot.py && break
sleep 3;
done