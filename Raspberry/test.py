import requests
import time
while True:
    try:
        requests.get(
            'http://smartdevgroup.hopto.org', timeout=1)
        internet_status = True
        print("true")
    except requests.exceptions.RequestException:
        internet_status = False
    time.sleep(5)
