import requests
import time

# data = requests.get(
#    'http://smartdevgroup.hopto.org/service/raspi.php?api=123456789&con=first')
data = requests.get(
    'http://smartdevgroup.hopto.org/service/raspi.php?api=123456789')
data_old = data.json()
print(data_old)
keys = data_old.keys()
t_time = time.time()
temp_data = 22

while True:
    data = requests.get(
        'http://smartdevgroup.hopto.org/service/raspi.php?api=123456789')
    data = data.json()

    for key in keys:
        if data[key]["value"] != data_old[key]["value"]:
            data_old[key].update({'value': data[key]["value"]})
            url = "http://"
            url += data[key]["ip"]
            url += "/?status="
            url += data[key]["value"]
            # r eqToESP = requests.get(url)
            print(url)
