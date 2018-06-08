#!/bin/bash
export LC_ALL=C
sudo apt-get install python-pip
pip install tornado
pip install psutil
pip install requests
pip install tcconfig
sudo setcap cap_net_admin+ep /sbin/tc
sudo setcap cap_net_raw,cap_net_admin+ep /bin/ip
sudo setcap cap_net_raw,cap_net_admin+ep /sbin/xtables-multi
