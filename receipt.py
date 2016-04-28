from google.appengine.ext import ndb

class Receipt(ndb.Model):
	user = ndb.StringProperty(required = True)
	concept = ndb.StringProperty()
	price = ndb.FloatProperty()
	date = ndb.DateProperty()