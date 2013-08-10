import json

import webapp2

from model.event import EventModel

class SingleEventHandler(webapp2.RequestHandler):

	def get(self, event_id):
		"get the whole activities of the specified event"
		event = EventModel.query().fetch()
		self.response.headers['Content-Type'] = 'application/json'
		self.response.out.write(event)
		

	def post(self, event_id):
		"Revise the tips for one of the activities in the event"
		pass