import webapp2
import os
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

import time

from task import Task

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class DeleteTaskHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')
			
			# Get receipt id
			idTask = self.request.get('idTask', '')

			if idTask == '':
				self.redirect('/error?error=La tarea no existe :(')
				return
			else:
				# Get query from database
				task = ndb.Key(urlsafe = idTask).get()

				if task == None:
					self.redirect('/error?error=La tarea no existe :(')
					return
				else:
					# Delete id
					task.key.delete()

					time.sleep(1)

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