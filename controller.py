import json
import os
import logging
from datetime import datetime
from google.appengine.ext import ndb

import webapp2

from model import Activity, Reminder, dummyEvent

class MainPage(webapp2.RequestHandler):

    def get(self):
        de = {}
        de['project Name'] = 'Hello, Diabetes and Hajj!'
        de["activitylist"] = dummyEvent.activitylist
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(de))

class EventListHandler(webapp2.RequestHandler):

    def get(self):
        evnet_list = ["Hajj", "Burning Man"]
        self.response.out.write(json.dumps(evnet_list))

class EventHandler(webapp2.RequestHandler):

    def get(self, event_name):
        ancestor_key = ndb.Key("Event", event_name)
        all_activities = Activity.all_activities(ancestor_key)
        self.response.headers['Content-Type'] = 'application/json'
        if all_activities.count() == 0:
            empty_reminder = {"Empty Datastore": "No activities for " + event_name + " availbe"}
            self.response.out.write(json.dumps(empty_reminder))
        else:
            self.response.out.write(json.dumps([a.to_dict() for a in all_activities]))

    def post(self, event_name):
        activity_obj = json.loads(self.request.body)
        activity = Activity(
            parent=ndb.Key("Event", event_name),
            activityName=activity_obj["activityName"],
            startDateTime=activity_obj["startDateTime"],
            endDateTime=activity_obj["endDateTime"],
            routes=activity_obj["routes"],
            activityRelatedTips=activity_obj["activityRelatedTips"],
            generalHealthTips=activity_obj["generalHealthTips"],
            diabetesSpecificHealthTips=activity_obj["diabetesSpecificHealthTips"],
            aidInfomations=activity_obj["aidInfomations"],
            dietRecommendations=activity_obj["dietRecommendations"],
            relationToOtherActivities=activity_obj["relationToOtherActivities"])
        activity.put()
        self.response.out.write(json.dumps({"200":"Activity stored successfully."}))

SIMPLE_TYPES = (int, long, float, bool, dict, basestring, list)

# def to_dict(model):
#     output = {}

#     for key, prop in model.properties().iteritems():
#         value = getattr(model, key)

#         if value is None or isinstance(value, SIMPLE_TYPES):
#             output[key] = value
#         elif isinstance(value, datetime.date):
#             # Convert date/datetime to MILLISECONDS-since-epoch (JS "new Date()").
#             ms = time.mktime(value.utctimetuple()) * 1000
#             ms += getattr(value, 'microseconds', 0) / 1000
#             output[key] = int(ms)
#         elif isinstance(value, db.GeoPt):
#             output[key] = {'lat': value.lat, 'lon': value.lon}
#         elif isinstance(value, db.Model):
#             output[key] = to_dict(value)
#         else:
#             raise ValueError('cannot encode ' + repr(prop))

#     return output

