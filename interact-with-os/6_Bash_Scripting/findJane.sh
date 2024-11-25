#!/bin/bash

>oldFiles.txt

files=$(grep " jane " "./data/list.txt" | cut -d' ' -f 3)
# echo $files

for file in $files; do
    # echo $file
    if test -e ".$file"; then 
        echo ".$file">>oldFiles.txt;
    else
        echo "File not found";
    fi
done