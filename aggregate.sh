#!/bin/bash
xzcat stats/*.csv.xz 2>/dev/null | ./decode.py | grep -o "[^,]*,[^,]*201508" | sort | uniq -c | sort -h
for i in stats/*.csv.xz; do echo "$i" $(xzcat "$i" 2>/dev/null| wc -l); done

