import webapp2
import json
import logging

from model.event import EventModel
from helper import json2model, model2json

class SingleEventHandler(webapp2.RequestHandler):

    def get(self, event_id):
        "get the whole activities of the specified event"
        event_model = EventModel.query(EventModel.eid == int(event_id)).get()
        event_obj = model2json(event_model) if event_model else None
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(event_obj)
        

    def post(self, event_id):
        "Revise the tips for one of the activities in the event"
        activity_object = json.loads(self.request.body)
        event_model = EventModel.query(EventModel.eid == int(event_id)).get()
        logging.info('Fetched Event Model ID: %s', event_model.eid)

        for a in event_model.activity_list:
            # logging.info('Activity %s tips: %s', a.aid, a.tips)
            logging.info("%s = %s, %s", a.aid, activity_object["ID"], a.aid == int(activity_object["ID"]))
            if a.aid == int(activity_object["ID"]):
                a.tips = activity_object["Tips"]
                logging.info('Activity %s tip changed: %s', a.aid, a.tips)

        event_model.put()
        self.response.out.write("OK")