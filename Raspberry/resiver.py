import requests

data = requests.get(
    'http://smartdevgroup.hopto.org/service/raspi.php?api=123456789')
data_old = data.json()
print(data_old)

keys = data_old.keys()


while True:
    data = requests.get(
        'http://smartdevgroup.hopto.org/service/raspi.php?api=123456789')
    data = data.json()
    for key in keys:
        if data[key]["value"] != data_old[key]["value"]:
            data_old[key].update({'value': data[key]['value']})
            url = "http://"
            url += data[key]["ip"]
            url += "/?status="
            url += data[key]["value"]
            # reqToESP = requests.get(url)
            print(url)
