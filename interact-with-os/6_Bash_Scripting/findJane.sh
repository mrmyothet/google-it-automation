#!/bin/bash

>oldFiles.txt

files=grep " jane " ./data/list.txt | cut -d' ' -f 1,3
for file in files; do
    echo $file>>oldFiles.txt
done