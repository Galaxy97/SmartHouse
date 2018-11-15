import json
import requests
import urllib2
import time
import threading

global internet_status
internet_status = True
first_connection = True
global serial
serial = "12345678910"
global accId


def thread(my_func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper


def load_json():
    with open('setting.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def write_json(data):
    with open('setting.json', 'w', encoding='utf-8') as fh:
        json.dump(data, fh, indent=3)
    return data


@thread
def internet():
    global internet_status
    while True:
        try:
            urllib2.urlopen('http://smartdevgroup.hopto.org', timeout=1)
            internet_status = True
        except urllib2.URLError:
            internet_status = False
    time.sleep(5)


while True:
    if first_connection:
        print("in while")
        first_connection = False
        global serial
        url = "http://smartdevgroup.hopto.org/"
        url += "service/add_brain.php?serial="
        url += str(serial)
        data = requests.get(url).text
        # data = data.text
        print("data is :")
        print(data)
        if(data == ""):
            print("data = ' '")
            time.sleep(1)
            data = requests.get(url).text
            print("data is :")
            print(data)
        if(data == "repeat"):
            print("data = 'repeat'")
            while data == "repeat":
                print("data = 'repeat in loop'")
                data = requests.get(url).text
                time.sleep(3)
            global accId
            accId = data
            print(accId)

    if internet_status:
        pass
