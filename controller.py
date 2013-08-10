import json
import os
import logging
import datetime
import requests
from google.appengine.ext import ndb

from helper import MyEncoder

import webapp2

from model import Event, Activity, Reminder, User

class MainPage(webapp2.RequestHandler):

    def get(self):
        de = {}
        de['project Name'] = 'Hello, Diabetes and Hajj!'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(de))

class EventListHandler(webapp2.RequestHandler):

    def get(self):
        events = Event.query().fetch()
        print events
        self.response.headers['Content-Type'] = 'application/json'
        # if events.count() == 0:
        #     empty_reminder = {"Empty Event List": "No events for " + event_id + " available"}
        #     self.response.out.write(json.dumps(empty_reminder))
        # else:
            # forecast = requests.get("https://api.forecast.io/forecast/" + 
            #     FORECAST_APIKEY +"/37.8267,-122.423")
        event_list = []
        for e in events:
            e_dict = e.to_dict()
            # result = forecast.json()
            # a_dict["weather"] = result
            event_list.append(e_dict)
        self.response.out.write(json.dumps(event_list, cls=MyEncoder))

    def post(self):
        event_list = json.loads(self.request.body)
        print event_list, "\n\n type:", type(event_list)
        for e in event_list["eventList"]:
            Event(eventName=e["eventName"], eventBrief=e["eventBrief"]).put()


class EventHandler(webapp2.RequestHandler):

    def get(self, event_id):
        FORECAST_APIKEY = "0daceb1cb82c10ac44a5850b009b2124"
        ancestor_key = ndb.Key("Event", event_id)
        all_activities = Activity.all_activities(ancestor_key)
        self.response.headers['Content-Type'] = 'application/json'
        if all_activities.count() == 0:
            empty_reminder = {"Empty Datastore": "No activities for " + event_id + " available"}
            self.response.out.write(json.dumps(empty_reminder))
        else:
            # forecast = requests.get("https://api.forecast.io/forecast/" + 
            #     FORECAST_APIKEY +"/37.8267,-122.423")
            activity_list = []
            for a in all_activities:
                a_dict = a.to_dict()
                # result = forecast.json()
                # a_dict["weather"] = result
                activity_list.append(a_dict)
            self.response.out.write(json.dumps(activity_list, cls=MyEncoder))

    def post(self, event_id):
        activity_obj = json.loads(self.request.body)
        activity = Activity(
            parent=ndb.Key("Event", event_id),
            activityName=activity_obj["activityName"],
            createDateTime=datetime.now(),
            activityTips=activity_obj["activityTips"] if "activityTips" in activity_obj else None,
            healthTips=activity_obj["healthTips"] if "healthTips" in activity_obj else None,
            relationToOtherActivities=activity_obj["relationToOtherActivities"] if "relationToOtherActivities" in activity_obj else None)
        activity.put()
        self.response.out.write(json.dumps({"200":"Activity stored successfully.",
            "Details": activity_obj}))

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

class UserHandler(webapp2.RequestHandler):

    def get(self, uid):
        user =  User.get_by_id(uid)
        uobj = {}
        uobj["userID"] = user.uid
        uobj["userEmail"] = user.uemail
        uobj["userPassward"] = user.upwd
        self.response.out(json.dumps(uobj))

class RegisterHandler(webapp2.RequestHandler):

    def post(self):
        uobj = json.loads(self.request.body)
        user = User(uid=uobj["userID"], uemail=uobj["userEmail"], upwd=uobj["userPassward"])
        user.put()
        resobj = {"user create": "succeed"}
        self.response.out.write(json.dumps(resobj))


