import os

import webapp2

from controller import MainPage, EventListHandler, EventHandler, UserHandler, RegisterHandler


# debug = os.environ.get('SERVER_SOFTWARE', '').startwith('Dev')

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=MainPage, name='home'),
    webapp2.Route(r'/register', handler=RegisterHandler),
    webapp2.Route(r'/login/<uid:\d+>', handler=UserHandler),
    webapp2.Route(r'/events', handler=EventListHandler, name='event_list'),
    webapp2.Route(r'/event/<event_id:\w+>', handler=EventHandler, name='event'),
], debug=True)

# if __name__ == "__main__":
#     main()