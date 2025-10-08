import requests
import json

with open(r'samruk/global_options.txt', 'r') as f:
    ecp_password = str(f.readline().split('=')[-1].replace(' ', '').replace('\n', ''))
    portal_password = str(f.readline().split('=')[-1].replace(' ', '').replace('\n', ''))
    address = str(f.readline().split('=')[-1].replace(' ', '').replace('\n', ''))
    iik = str(f.readline().split('=')[-1].replace(' ', '').replace('\n', ''))
    number_for_copy = str(f.readline().split('=')[-1].replace(' ', '').replace('\n', ''))
    from_lot = str(f.readline().split('=')[-1].replace(' ', '').replace('\n', ''))
    sec_cat_val = str(f.readline().split('=')[-1].replace(' ', '').replace('\n', ''))
    company_name = str(f.readline().split('=')[-1].replace(' ', '').replace('\n', ''))
    etsp = str(f.readline().split(' = ')[-1])


key_pass = ecp_password
key = etsp
def xml_sign_sk(key_value, port = 14579, host_ip = 'localhost'):
    url = f"http://{host_ip}:{port}/xml/sign"

    payload = json.dumps({
    "xml": key_value,
    "signers": [
        {
        "key": etsp,
        "password": key_pass,
        "keyAlias": None
        }
    ],
    "clearSignatures": False,
    "trimXml": False
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    return response.json()['xml']
