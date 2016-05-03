import webapp2
import os
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

import time

from schedule import Schedule

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class AddFieldScheduleHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')

			template_values = {
				'user_name' : user_name,
				'access_link' : access_link,
			}

			template = JINJA_ENVIRONMENT.get_template('addFieldSchedule.html')
			self.response.write(template.render(template_values));
		else:
			self.redirect('/')

	def post(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')

			# Get values from inputs and save into database
			day = self.request.get('day')
			hourStart = int(self.request.get('hourStart'))
			minStart = int(self.request.get('minStart'))
			hourEnd = int(self.request.get('hourEnd'))
			minEnd = int(self.request.get('minEnd'))
			task = self.request.get('task')

			# Store data into database
			schedule = Schedule()

			schedule.user = user.user_id()

			schedule.day = day
			schedule.hourStart = hourStart
			schedule.minStart = minStart
			schedule.hourEnd = hourEnd
			schedule.minEnd = minEnd
			schedule.task = task

			schedule.put()

			time.sleep(1)

			# Get query from database
			monday = Schedule.query(Schedule.user == user.user_id()).filter(Schedule.day == 'lunes')
			tuesday = Schedule.query(Schedule.user == user.user_id()).filter(Schedule.day == 'martes')
			wednesday = Schedule.query(Schedule.user == user.user_id()).filter(Schedule.day == 'miercoles')
			thursday = Schedule.query(Schedule.user == user.user_id()).filter(Schedule.day == 'jueves')
			friday = Schedule.query(Schedule.user == user.user_id()).filter(Schedule.day == 'viernes')
			saturday = Schedule.query(Schedule.user == user.user_id()).filter(Schedule.day == 'sabado')
			sunday = Schedule.query(Schedule.user == user.user_id()).filter(Schedule.day == 'domingo')

			template_values = {
				'user_name' : user_name,
				'access_link' : access_link,
				'monday' : monday,
				'tuesday' : tuesday,
				'wednesday' : wednesday,
				'thursday' : thursday,
				'friday' : friday,
				'saturday' : saturday,
				'sunday' : sunday
			}

			template = JINJA_ENVIRONMENT.get_template('showSchedule.html')
			self.response.write(template.render(template_values));
		else:
			self.redirect('/')