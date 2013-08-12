import json
from ast import literal_eval

from model.event import EventModel, Activity, Relation, Place

def json2model(event_obj):
    print event_obj
    event_obj = json.loads(event_obj.replace('\r\n', '\\r\\n'))
    id = int(event_obj["ID"])
    event = EventModel.query(EventModel.eid == id).get()
    if not event:
        event = EventModel()
    event.eid = int(event_obj["ID"])
    event.name = event_obj["Name"]
    event.brief = event_obj["Brief"]
    event.start_date = event_obj["Start Date"]
    event.duration = event_obj["Duration"]
    event.activity_list = []
    for a in event_obj["Activity List"]:
        activity = Activity()
        activity.aid = int(a["ID"])
        activity.name = a["Name"]
        activity.start_date = a["Start Date"]
        activity.duration = a["Duration"]
        activity.place = Place();
        activity.place.name = a["Place"]["Name"]
        activity.place.location = a["Place"]["Location"]
        activity.tips = a["Tips"]
        activity.relation = Relation()
        activity.relation.previous = a["previous"]
        activity.relation.next = a["next"]
        activity.relation.xor = a["xor"]
        event.activity_list.append(activity)
    event.before_you_go = str(event_obj["Before You Go"])
    event.general_tips = event_obj["General Tips"]
    return event

def model2json(event_model):
    event = {}
    event["ID"] = event_model.eid
    event["Name"] = event_model.name
    event["Brief"] = event_model.brief
    event["Start Date"] = event_model.start_date
    event["Duration"] = event_model.duration
    event["Activity List"] = []
    a1 = []
    for a2 in event_model.activity_list:
        a1 = {
        "ID" : a2.aid,
        "Name" : a2.name,
        "Start Date" : a2.start_date,
        "Duration" : a2.duration,
        "Place" : {
            "Name": a2.place.name,
            "Location": a2.place.location,
            "Weather": a2.place.weather
            },
        "Tips": a2.tips,
        "Relation": {
            "previous": a2.relation.previous,
            "next": a2.relation.next,
            "xor": a2.relation.xor
            }
        }
        event["Activity List"].append(a1)
    event["Before You Go"] = literal_eval(event_model.before_you_go)
    event["General Tips"] = event_model.general_tips
    return json.dumps(event)



