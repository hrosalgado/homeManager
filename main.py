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

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
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
    ('/deleteReceipt', DeleteReceiptHandler)
], debug=True)
