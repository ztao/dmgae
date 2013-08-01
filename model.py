from google.appengine.ext import ndb

class Activity(ndb.Model):
    #build a model for each activity in an event
    activityName = ndb.StringProperty()
    startDateTime = ndb.JsonProperty()
    endDateTime = ndb.JsonProperty()
    # routes will be a list
    routes = ndb.JsonProperty()
    # weather = ndb.StringProperty()
    # tempreture = ndb.IntegerProperty()
    activityRelatedTips = ndb.JsonProperty()
    generalHealthTips = ndb.JsonProperty()
    diabetesSpecificHealthTips = ndb.JsonProperty()
    aidInfomations = ndb.JsonProperty()
    dietRecommendations = ndb.JsonProperty()
    relationToOtherActivities = ndb.JsonProperty()

    @classmethod
    def all_activities(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(-cls.startDateTime)

class Reminder(ndb.Model):
    reminderName = ndb.StringProperty()
    reminderContent = ndb.StringProperty()
    reminderTrigger = ndb.JsonProperty()

# for the purpose of testing
class dummyEvent:
    activitylist = []
    activitylist.append({
        "activityName": "Activity A",
        "location": "London",
        "routingMethod": "South west service train",
        "weather": "Sunny!!",
        "activityTips": [
            "Bring enough money",
            "Enjoy",
            "Anything else?"
        ],
        "healthTips": [
            "Not yet"
        ]
    })
    activitylist.append({
        "activityName": "Activity B",
        "location": "Eidinburgh",
        "routingMethod": "horse",
        "weather": "Cloudy!!",
        "activityTips": [
            "Bring enough pounds",
            "Enjoy",
            "Anything else?"
        ],
        "healthTips": [
        ]
    })