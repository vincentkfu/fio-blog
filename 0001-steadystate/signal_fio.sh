#! /bin/bash

#
# Send the USR1 signal to the first (main) fio process every 20s
# Fio will do a summary output in response to each signal
#

pid=$(pidof fio | rev | cut -d " " -f1 | rev)

while [ $? -eq 0 ]; do
	sleep 20
	kill -s USR1 $pid
done
