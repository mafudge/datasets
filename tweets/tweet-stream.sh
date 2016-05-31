#!/bin/bash
max=100
for i in `seq 1 $max`;
do
	rnd=$(( ( RANDOM % 10 )  + 1 ))
	echo "Loop: $i of $max: Generating $rnd Tweets..."
	python simtweet.py -c $rnd -s "1/1/2015 12:00 AM" -e "12/31/2015 11:59 PM" -f psv >> sample-tweet-stream.psv
	sleep 10
done 

