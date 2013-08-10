from google.appengine.ext import ndb

class Place(ndb.Model):
    name = ndb.StringProperrty()
    location = ndb.GeoPtProperty()
    weather = ndb.StringProperrty()

class Activity(ndb.Model):
    name = ndb.StringProperrty()
    start_date = ndb.DateTimeProperty()
    duration = ndb.StringProperrty()
    place = ndb.StructuredProperty(Place)
    tips = ndb.TextProperty()
    relation = ndb.StructuredProperty(Relation)

class Event(ndb.Model):
    name = ndb.StringProperrty()
    brief =  = ndb.StringProperty()
    start_date = ndb.DateTimeProperty()
    duration = ndb.StringProperrty()
    activity_list = ndb.StructuredProperty(Activity, repeated=True)
    before_you_go = ndb.TextProperty()
    general_tips = ndb.TextProperty()

    @classmethod
    def query_activity_list(cls, ancestor_key):
        # ancestor_key will be the name of corresponding event
        return cls.query(ancestor=ancestor_key).order(-cls.activity_list.start_date)

