import requests
import time


from functions import sign
from functions.sign import *


def authorization():
    url = "https://zakup.sk.kz/eprocuaa/api/token"
    session = requests.Session()
    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru',
        'app-code-name': 'Mozilla',
        'app-name': 'Netscape',
        'cache-control': 'no-cache',
        'dnt': '1',
        'e-tag': 'MTMxNzQxMzI3Mjg4OA==',
        'language': 'ru',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'product-sub': '20030107',
        'referer': 'https://zakup.sk.kz/',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'tor': 'VzlNVE16TXpZMU5qSTBORFkzTXc9PXM2NjQ4MzM0NDIyMDI1MDYyMA==',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Cookie': 'Path=/; Path=/; _fbp=fb.1.1750370581175.236801882409544119; _ym_uid=1750370582355705751; _ym_d=1750370582; _ym_isad=1; Path=/'
        }
    session.headers = headers
    response = session.get(url, data=payload, verify=False)
    data = response.json()
    xml_to_sign = data['token']
    signed_xml = sign.xml_sign_sk(xml_to_sign)
    # TODO: import from payload, and update
    payload = {
        'grant_type': 'password',
        'password': f'{portal_password}',
        'username': signed_xml,
        'g-recaptcha-response': 'undefined',
        'type': 'NCALAYER'
    }

    # TODO: payload
    response = session.post('https://zakup.sk.kz/eprocuaa/oauth/token',
                            headers={'Content-Type': 'application/x-www-form-urlencoded',
                                     'Authorization': 'Basic d2ViX2FwcDo='}, data=payload, verify=False)
    print(portal_password)
    print(company_name)

    return response.json()['access_token']


def create_app(session, protocol_id, lot_id):
    start = time.time()
    url = f"https://zakup.sk.kz/eproctender/api/participations-ext/participation/{protocol_id}"
    payload = json.dumps(lot_id)
    # wait until the app opens
    while True:
        s = time.time()
        response = session.post(url, data=payload, verify=False)
        # print(response.text)
        print(response.status_code)
        print(time.time() - s)
        if response.status_code == 200:
            break
        
    response_dict = response.json()
    # get app_id
    app_id = response_dict['id']

    print(f'Create {app_id} app time is = ', time.time()-start)
    return app_id
    





