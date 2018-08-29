#! /bin/bash

proc_name="test_service"
while true 
do
	proc_num()
	{
		num=`ps -ef | grep $proc_name | grep -v grep | wc -l`
		return $num
	}
	
	proc_num  
	number=$?
	if [ $number -eq 0 ]          
	then
		cd /home/ubuntu/ontology/test_service/; ./run.sh -c 1
	fi 
	sleep 5
done