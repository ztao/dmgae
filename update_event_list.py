import json
import requests

def update_event_list():
    # url = "http://localhost:8080/events"
    url = "http://diabeteselsewhere.appspot.com/events"
    with open("event_list.json") as event_list:
        r = requests.post(url, event_list.read())

if __name__ == '__main__':
    update_event_list()