from google.appengine.ext import ndb

class Place(ndb.Model):
    name = ndb.StringProperty()
    location = ndb.GeoPtProperty()
    weather = ndb.StringProperty()

class Relation(ndb.Model):
    previous = ndb.StringProperty()
    next = ndb.StringProperty()
    xor = ndb.StringProperty()

class Activity(ndb.Model):
    aid = ndb.IntegerProperty()
    name = ndb.StringProperty()
    start_date = ndb.StringProperty()
    duration = ndb.StringProperty()
    place = ndb.StructuredProperty(Place)
    tips = ndb.TextProperty()
    relation = ndb.StructuredProperty(Relation)

    @classmethod
    def all_activities(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(cls.aid)

class EventModel(ndb.Model):

    eid = ndb.IntegerProperty()
    name = ndb.StringProperty()
    brief = ndb.TextProperty()
    start_date = ndb.StringProperty()
    duration = ndb.StringProperty()
    activity_list = ndb.StructuredProperty(Activity, repeated=True)
    before_you_go = ndb.JsonProperty()
    general_tips = ndb.TextProperty()

    @classmethod
    def all_events(cls):
        return cls.query().order(cls.eid)
