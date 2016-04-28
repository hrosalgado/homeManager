import webapp2
import os
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

from receipt import Receipt

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class ShowReceiptHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')
			
			# Get query from database
			receipts = Receipt.query(Receipt.user == user.user_id()).order(-Receipt.date)

			template_values = {
				'user_name' : user_name,
				'access_link' : access_link,
				'receipts' : receipts
			}

			template = JINJA_ENVIRONMENT.get_template('showReceipt.html')
			self.response.write(template.render(template_values));
		else:
			self.redirect('/')