#!/bin/bash

FILE="/Users/tae/Documents/PROGRAMMING/Teach Yourself CS/1. SICP/1. Composing_programs.pdf"
CHUNK_SIZE=20 #number of pages per pdf

# Extract directory and filename
DIR=$(dirname "$FILE")
FILENAME=$(basename "$FILE")
BASENAME="${FILENAME%.*}"  # Remove .pdf extension

# Get total number of pages
PAGES=$(pdfinfo "$FILE" | grep Pages | awk '{print $2}')
COUNTER=0

for (( i=1; i<=PAGES; i+=CHUNK_SIZE ))
do
    START=$i
    END=$(( i+CHUNK_SIZE-1 ))
    if [ "$END" -gt "$PAGES" ]; then
        END=$PAGES
    fi

    OUTPUT="${DIR}/${BASENAME}_part_$((COUNTER+1)).pdf"
    pdfjam "$FILE" "$START-$END" -o "$OUTPUT"
    ((COUNTER++))
done
