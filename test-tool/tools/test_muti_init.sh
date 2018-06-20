python3 nodecontroll.py  -a stop -n 0,1,2,3,4,5,6
python3 nodecontroll.py  -a restart -n 0,1,2,3,4,5,6
sleep 10


cd ~/ontology/node
echo 123456 | ./transfer.sh ALp2zvAqN2pS8QejQtSDxw5aBQGHGaSKd4 ALp2zvAqN2pS8QejQtSDxw5aBQGHGaSKd4 10000000

sleep 3
echo 123456 | ./withdrawong.sh

sleep 3
cd ~/ontology/test/tools
python3 foo.py
