import webapp2
import os
import jinja2

from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class ErrorHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')
			
			try:
				error = self.request.get('error')
			except:
				error = 'Error :('

			template_values = {
				'user_name' : user_name,
				'access_link' : access_link,
				'error' : error
			}

			template = JINJA_ENVIRONMENT.get_template('error.html')
			self.response.write(template.render(template_values));
		else:
			self.redirect('/')