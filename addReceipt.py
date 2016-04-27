import webapp2
import os
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

from datetime import datetime
import time

from receipt import Receipt

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class AddReceiptHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')

			template_values = {
				'user_name' : user_name,
				'access_link' : access_link
			}

			template = JINJA_ENVIRONMENT.get_template('addReceipt.html')
			self.response.write(template.render(template_values));
		else:
			self.redirect('/')

	def post(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')

			# Get values from inputs and save into database
			concept = self.request.get('conceptReceiptAdd')
			price = float(self.request.get('priceReceiptAdd'))
			date = datetime.strptime(self.request.get('dateReceiptAdd'), '%Y-%m-%d')

			receipt = Receipt()

			receipt.concept = concept
			receipt.price = price
			receipt.date = date

			receipt.put()

			time.sleep(1)

			# Get query from database
			receipts = Receipt.query()

			template_values = {
				'user_name' : user_name,
				'access_link' : access_link,
				'receipts' : receipts
			}

			template = JINJA_ENVIRONMENT.get_template('showReceipt.html')
			self.response.write(template.render(template_values));
		else:
			self.redirect('/')