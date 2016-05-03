import webapp2
import os
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

import time

from shoppingList import ShoppingList

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class DeleteListHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.nickname()
			access_link = users.create_logout_url('/')
			
			# Get receipt id
			idShoppingList = self.request.get('idShoppingList', '')

			if idShoppingList == '':
				self.redirect('/error?error=La lista de la compra no existe :(')
				return
			else:
				# Get query from database
				shoppingList = ndb.Key(urlsafe = idShoppingList).get()

				if shoppingList == None:
					self.redirect('/error?error=La lista de la compra no existe :(')
					return
				else:
					# Delete id
					shoppingList.key.delete()

					time.sleep(1)

					# Get query from database
					shoppingLists = ShoppingList.query(ShoppingList.user == user.user_id()).order(-ShoppingList.date)

					template_values = {
						'user_name' : user_name,
						'access_link' : access_link,
						'shoppingLists' : shoppingLists
					}

					template = JINJA_ENVIRONMENT.get_template('showList.html')
					self.response.write(template.render(template_values));
		else:
			self.redirect('/')