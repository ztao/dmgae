import json
import datetime
import requests
import logging
from google.appengine.ext import ndb

import webapp2

from model.event import EventModel, Activity, Relation, Place
from helper import json2model

class EventListHandler(webapp2.RequestHandler):

    def get(self):
        events = EventModel.all_events().fetch()
        e_list = []
        event = {}
        for e in events:
            event["Name"] = e.name
            event["Brief"] = e.brief
            e_list.append(event)

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(e_list))

    def post(self):
        print self.request.body
        event_model = json2model(self.request.body)
        event_model.put()
