from google.appengine.ext import ndb

class Task(ndb.Model):
	user = ndb.StringProperty(required = True)
	name = ndb.StringProperty()
	items = ndb.StringProperty(repeated = True)
	date = ndb.DateProperty()
