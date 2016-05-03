import webapp2
import os
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

from datetime import datetime
import time

from task import Task

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class ShowTaskHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')

			# Get query from database
			tasks = Task.query(Task.user == user.user_id()).order(-Task.date)

			template_values = {
				'user_name' : user_name,
				'access_link' : access_link,
				'tasks' : tasks
			}

			template = JINJA_ENVIRONMENT.get_template('showTask.html')
			self.response.write(template.render(template_values));
		else:
			self.redirect('/')