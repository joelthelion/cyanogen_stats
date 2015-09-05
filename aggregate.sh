#!/bin/bash
xzcat stats/*.csv.xz 2>/dev/null | ./decode.py | cut -d, -f7,8,9 | grep -o ".*$(date +%Y%m)" | sort | uniq -c | sort -h
for i in stats/*.csv.xz; do echo "$i" $(xzcat "$i" 2>/dev/null| wc -l); done

