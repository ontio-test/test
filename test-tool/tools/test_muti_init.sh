python3 nodecontroll.py  -a stop -n 0,1,2,3,4,5,6
python3 nodecontroll.py  -a restart -n 0,1,2,3,4,5,6
sleep 10

cd ~/ontology/test/tools
python3 foo.py
