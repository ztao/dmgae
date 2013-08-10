import json
import datetime
from time import mktime

class MyEncoder(json.JSONEncoder):


    def default(self, obj):
        print obj
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))

        return json.JSONEncoder.default(self, obj)