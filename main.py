import webapp2
import os
import jinja2

from google.appengine.api import users

from home import HomeHandler
from addReceipt import AddReceiptHandler
from showReceipt import ShowReceiptHandler
from readReceipt import ReadReceiptHandler
from updateReceipt import UpdateReceiptHandler
from deleteReceipt import DeleteReceiptHandler
from error import ErrorHandler
from addList import AddListHandler
from showList import ShowListHandler
from readList import ReadListHandler
from updateList import UpdateListHandler
from deleteList import DeleteListHandler
from addTask import AddTaskHandler
from showTask import ShowTaskHandler
from readTask import ReadTaskHandler
from updateTask import UpdateTaskHandler
from deleteTask import DeleteTaskHandler
from showSchedule import ShowScheduleHandler
from addFieldSchedule import AddFieldScheduleHandler
from readFieldSchedule import ReadFieldScheduleHandler
from updateFieldSchedule import UpdateFieldScheduleHandler
from deleteFieldSchedule import DeleteFieldScheduleHandler

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        access_link = 0

    	user = users.get_current_user()

    	if(user != None):
    		self.redirect('/home')
    	else:
    		access_link = users.create_login_url('/home')

    	template_values = {
    		'access_link' : access_link
    	}

    	template = JINJA_ENVIRONMENT.get_template('index.html')
    	self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/home', HomeHandler),
    ('/addReceipt', AddReceiptHandler),
    ('/showReceipt', ShowReceiptHandler),
    ('/readReceipt', ReadReceiptHandler),
    ('/updateReceipt', UpdateReceiptHandler),
    ('/deleteReceipt', DeleteReceiptHandler),
    ('/error', ErrorHandler),
    ('/addList', AddListHandler),
    ('/showList', ShowListHandler),
    ('/readList', ReadListHandler),
    ('/updateList', UpdateListHandler),
    ('/deleteList', DeleteListHandler),
    ('/addTask', AddTaskHandler),
    ('/showTask', ShowTaskHandler),
    ('/readTask', ReadTaskHandler),
    ('/updateTask', UpdateTaskHandler),
    ('/deleteTask', DeleteTaskHandler),
    ('/showSchedule', ShowScheduleHandler),
    ('/addFieldSchedule', AddFieldScheduleHandler),
    ('/readFieldSchedule', ReadFieldScheduleHandler),
    ('/updateFieldSchedule', UpdateFieldScheduleHandler),
    ('/deleteFieldSchedule', DeleteFieldScheduleHandler)
], debug=True)
