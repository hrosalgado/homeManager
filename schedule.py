from google.appengine.ext import ndb

class Schedule(ndb.Model):
	user = ndb.StringProperty(required = True)
	day = ndb.StringProperty()
	hourStart = ndb.IntegerProperty()
	minStart = ndb.IntegerProperty()
	hourEnd = ndb.IntegerProperty()
	minEnd = ndb.IntegerProperty()
	task = ndb.StringProperty()