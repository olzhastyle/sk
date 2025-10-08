import requests
import time
import threading
import datetime

import sys
sys.path.append('.')
import functions.global_functions as func
import functions.config as cfg


number_anno = 1150401
lot_id = [
    4181576,
    ]
obespechenie = [
    47736,
]
obespechenie_dict = {   
    4181576: 47736,
}

######################################################################################################################
#START APPLICATION#
session = requests.Session()
session.headers = cfg.headers
session.headers['Authorization'] = f'Bearer {func.authorization()}'

app_id_requirement_ids = None

app_id = func.create_app(session, number_anno, lot_id)


def get_req_id():
    global app_id_requirement_ids
    start_time = datetime.datetime.now()
    print('req id time = ', start_time)
    while not app_id:
        time.sleep(0)
    app_id_requirement_url = f'https://zakup.sk.kz/eproctender/api/participations/{app_id}/lots?page=0&size=10&sort=id,asc'
    response = session.get(app_id_requirement_url, verify=False)

    app_id_requirement_ids = response.json()
    print('req got id = ', datetime.datetime.now())
    print(app_id_requirement_ids)
    return app_id_requirement_ids

req_id_thread = threading.Thread(target=get_req_id, args=())
req_id_thread.start()


reqs_threads = []
for lot in app_id_requirement_ids:
    app_id_requirement_id = lot['id']
    lot_id_s = lot['lot']['id']
    req_criteria_time = time.time()
    # Proccessing requirements and criterias page
    # requirements_and_criterias(session=session, app_id_requirement_id=app_id_requirement_id,
    #                         headers_put=headers_put, obespechenie=obespechenie_dict[lot_id_s])
    reqs = threading.Thread(target=requirements_and_criterias, args=(session, app_id_requirement_id, headers_put, req_etag, req_tor, obespechenie_dict[lot_id_s],))
    reqs.start()
    reqs_threads.append(reqs)
    print(f"Requirements and criterias filled in {time.time() - req_criteria_time}")