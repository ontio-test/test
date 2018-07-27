echo "run test_auth"
cd test_auth
python3 test_main.py

echo "run test_benefit_model"
cd ../test_benefit_model
python3 test_main.py

echo "run test_consensus"
cd ../test_consensus
python3 test_main.py

echo "run test_governance"
cd ../test_governance
python3 test_main.py

echo "run test_governance_api"
cd ../test_governance_api
chmod 777 run.sh
./run.sh

echo "run test_muti_contract"
cd ../test_muti_contract
python3 test_main.py

echo "run test_neo_api"
cd ../test_neo_api
python3 test_main.py

echo "run test_neo_param"
cd ../test_neo_param
python3 test_main.py

echo "run test_ong_native"
cd ../test_ong_native
python3 test_main.py

echo "run test_ont_native"
cd ../test_ont_native
python3 test_main.py

echo "run test_web_api..."
cd test_web_api
python3 test_restful.py
python3 test_rpc.py
python3 test_websocket.py

echo "run test_cost"
cd ../test_cost
python3 test_main.py

echo "run test_erncryption"
cd ../test_erncryption
python3 test_main.py

echo "run test_ontid_api"
cd ../test_ontid_api
python3 test_ontid.py
python3 test_ontid_neo.py

echo "run test_ontid_others"
cd ../test_ontid_others
python3 test_main.py
