#!/bin/bash

# Read from the file file.txt and print its transposed content to stdout.

cols=$(head -n1 file.txt | awk '{print NF}')

for i in $(seq 1 $cols); do
    cut -d' ' -f$i file.txt | paste -sd' '
done
