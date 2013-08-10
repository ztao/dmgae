import json
import datetime
import requests
from google.appengine.ext import ndb

import webapp2

from model.event import EventModel, Activity, Relation, Place

class EventListHandler(webapp2.RequestHandler):

    def get(self):
        event = EventModel.all_events().fetch()
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(event)

    def post(self):
        event_obj = json.loads(self.request.body)
        event = Event()
        event.eid = event_obj["ID"]
        event.name = event_obj["Name"]
        event.brief = event_obj["Brief"]
        event.start_date = event_obj["Start Date"]
        event.duration = event_obj["Duration"]
        event.activity_list = []
        for a in event_obj["Activity List"]:
            activity = Activity()
            activity.aid = a["ID"]
            activity.name = a["Name"]
            activity.start_date = a["Start Date"]
            activity.duration = a["Duration"]
            activity.place = a["Place"]
            activity.tips = a["Tips"]
            activity.relation = Relation()
            activity.relation.previous = a["previous"]
            activity.relation.next = a["next"]
            activity.relation.xor = a["xor"]
            event.activity_list.append(activity)
        event.before_you_go = str(event_obj["Before You Go"])
        event.general_tips = event_obj["General Tips"]