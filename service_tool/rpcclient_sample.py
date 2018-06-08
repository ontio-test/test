import requests
import json


def main():
    url = "http://139.219.136.15:23635/jsonrpc"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "get_states_md5",
        "params": {},
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print(json.dumps(response))


if __name__ == "__main__":
    main()
