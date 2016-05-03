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

class ReadReceiptHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')
			
			# Get receipt id
			idReceipt = self.request.get('idReceipt', '')

			if idReceipt == '':
				self.redirect('/error?error=El ticket no existe :(')
				return
			else:
				# Get query from database
				receipt = ndb.Key(urlsafe = idReceipt).get()

				if receipt == None:
					self.redirect('/error?error=El ticket no existe :(')
					return
				else:
					template_values = {
						'user_name' : user_name,
						'access_link' : access_link,
						'receipt' : receipt
					}

					template = JINJA_ENVIRONMENT.get_template('readReceipt.html')
					self.response.write(template.render(template_values));
		else:
			self.redirect('/')