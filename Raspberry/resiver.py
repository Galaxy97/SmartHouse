import requests
import time

data = requests.get(
    'http://smartdevgroup.hopto.org/service/raspi.php?api=123456789')
data_old = data.json()
print(data_old)
keys = data_old.keys()
t_time = time.time()
temp_data = 22

while True:
    if (time.time() - t_time > 2.0):
        url = "http://"
        url += "192.168.0.55/Sensor"
        reqToESP = requests.get(url)
        temp_data = reqToESP.text
        t_time = time.time()

    global_url = "http://smartdevgroup.hopto.org"
    global_url += "/service/raspi.php?api=123456789&temp="
    global_url += str(temp_data)
    
    data = requests.get(global_url)
    data = data.json()

    for key in keys:
        if data[key]["value"] != data_old[key]["value"]:
            data_old[key].update({'value': data[key]["value"]})
            url = "http://"
            url += data[key]["ip"]
            url += "/?status="
            url += data[key]["value"]
            reqToESP = requests.get(url)
            print(url)
