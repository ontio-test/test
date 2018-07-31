killall run_alltest
python3 -u run_alltest.py -c select.json > `date +%F_%H_%M_%S`.log  &
