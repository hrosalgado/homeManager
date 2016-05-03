import webapp2
import os
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

import time

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class ReadFieldScheduleHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')

			# Get field schedule id
			idFieldSchedule = self.request.get('idFieldSchedule', '')

			if idFieldSchedule == '':
				self.redirect('/error?error=El campo del horario no existe :(')
				return
			else:
				# Get query from database
				fieldSchedule = ndb.Key(urlsafe = idFieldSchedule).get()

				if fieldSchedule == None:
					self.redirect('/error?error=El campo del horario no existe :(')
					return
				else:
					template_values = {
						'user_name' : user_name,
						'access_link' : access_link,
						'fieldSchedule' : fieldSchedule
					}

					template = JINJA_ENVIRONMENT.get_template('readFieldSchedule.html')
					self.response.write(template.render(template_values));
		else:
			self.redirect('/')