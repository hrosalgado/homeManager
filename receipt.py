from google.appengine.ext import ndb

class Receipt(ndb.Model):
	concept = ndb.StringProperty()
	price = ndb.FloatProperty()
	date = ndb.DateProperty()