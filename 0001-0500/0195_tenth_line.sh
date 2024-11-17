#!/bin/bash

# Read from the file file.txt and output the tenth line to stdout.

line_number=1

while IFS= read -r line; do
    if [[ "$line_number" =~ 10 ]]; then
        echo "$line"; break
    fi
    ((line_number++))
done < file.txt
