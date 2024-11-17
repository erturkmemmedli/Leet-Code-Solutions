#!/bin/sh

# Read from the file words.txt and output the word frequency list to stdout.

declare -A wordCount

while IFS= read -r line; do
    for word in $line; do
        ((wordCount["$word"]++))
    done
done < words.txt

for key in "${!wordCount[@]}"; do
    echo "$key ${wordCount[$key]}"
done | sort -k2,2nr -k1,1
