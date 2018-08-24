sudo apt-get install python3-pip
sudo apt-get install libssl-dev

pip3 install requests
pip3 install websocket-client
pip3 install base58
pip3 install ddt
pip3 install paramiko --user

chmod 777 tools/deploy_contract.sh
chmod 777 run_all.sh