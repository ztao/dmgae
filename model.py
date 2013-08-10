from google.appengine.ext import ndb
from webapp2_extras import Auth

class Event(ndb.Model):
    eventName = ndb.StringProperty()
    eventBrief = ndb.StringProperty()
    startDate = ndb.DateTimeProperty()
    # eventIcon: An Image!

class Activity(ndb.Model):
    #build a model for each activity in an event
    activityName = ndb.StringProperty()
    createDateTime = ndb.DateTimeProperty()   
    activityTips = ndb.JsonProperty()
    healthTips = ndb.JsonProperty()
    relationToOtherActivities = ndb.JsonProperty()

    @classmethod
    def all_activities(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(-cls.createDateTime)

class Reminder(ndb.Model):
    reminderName = ndb.StringProperty()
    reminderContent = ndb.StringProperty()
    reminderTrigger = ndb.JsonProperty()

class User(ndb.Model):
    uid = ndb.IntegerProperty()
    uemail = ndb.StringProperty()
    upwd = ndb.StringProperty()
