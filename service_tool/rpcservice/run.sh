killall test_service
python3 -u rpcserver.py > `date +%F_%H_%M_%S`.log 2>&1 &
