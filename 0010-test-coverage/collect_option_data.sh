#! /bin/bash
#
# - Clone fio 3.35 if it does not exist
# - Parse the HOWTO to obtain a list of fio commands
# - For each command search in the test scripts and direct the results to a file in the output directory named after the command
#

[ -d "fio-3.35" ] || git clone https://github.com/axboe/fio.git --depth=1 --branch fio-3.35 fio-3.35

grep ".. option::" fio-3.35/HOWTO.rst | cut -d ' ' -f3 | cut -d '=' -f 1 | sed 's/--//' | sed 's/,//' | sort | uniq > cmdlist.txt
readarray -t cmds < cmdlist.txt

for i in "${cmds[@]}"
do
	grep "$i" fio-3.35/t/*.py fio-3.35/t/zbd/* fio-3.35/t/jobs/*.fio > "output/$i"
done
