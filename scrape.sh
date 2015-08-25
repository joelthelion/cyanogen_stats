#!/bin/bash
while :
do
	./main.py | xz > "stats/stats_$(date).csv.xz"
	sleep 60
done
