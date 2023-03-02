#!/bin/sh

for day in /data/Twitter\ dataset/geoTwitter20-*; do
    nohup ./src/map.py "--input_path=$day" &
    #echo $day
done 
