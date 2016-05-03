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

class UpdateTaskHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')
			
			# Get shopping list id
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
					template_values = {
						'user_name' : user_name,
						'access_link' : access_link,
						'task' : task
					}

					template = JINJA_ENVIRONMENT.get_template('updateTask.html')
					self.response.write(template.render(template_values));
		else:
			self.redirect('/')

	def post(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')
			
			# Get Task id
			idTask = self.request.get('idTask')

			# Get query from database
			task = ndb.Key(urlsafe = idTask).get()

			# Update Task
			task.name = self.request.get('nameUpdateTask')
			
			items = list()
			numItems = self.request.get('numItems')
			for i in range(1, int(numItems) + 1):
				items.append(self.request.get('item' + str(i)))

			task.items = items

			# Save task
			task.put()

			time.sleep(1)

			template_values = {
				'user_name' : user_name,
				'access_link' : access_link,
				'task' : task
			}

			template = JINJA_ENVIRONMENT.get_template('readTask.html')
			self.response.write(template.render(template_values));
		else:
			self.redirect('/')