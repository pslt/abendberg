#!/bin/bash

now=$(date "+%Y%m%d_%H%M%S")
filename=$now.jpg

echo "Take picture."
raspistill -n -o $filename --width 1920 --height 1440 -a 4 -ae 50,0x99,0x00 -a "Ostermundigen %d.%m.%Y %X"

echo "Upload image to s3."
s3cmd -P put $filename s3://www.schilt.ch-smarthome/images/
s3cmd cp s3://www.schilt.ch-smarthome/images/$filename s3://www.schilt.ch-smarthome/images/latest.jpg

rm $filename
