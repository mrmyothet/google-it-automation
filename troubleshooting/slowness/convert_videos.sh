#!/bin/bash

# Remove daemonize from the command 
# Not to run paralle

echo "Starting video conversion"
for video in static/*.webm; do 
    mp4_video="$(echo "$video" | sed 's/\.webm$/.mp4/')"
    # daemonize -c $PWD /usr/bin/ffmpeg -nostats -nostdin -i "$video" "$mp4_video"
    /usr/bin/ffmpeg -nostats -nostdin -i "$video" "$mp4_video"
done