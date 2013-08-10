import json

import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        de = {}
        de['project Name'] = 'Hello, Diabetes and Hajj!'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(de))