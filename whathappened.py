#!/usr/bin/env python

import webapp2
import os

from google.appengine.api import users
from google.appengine.ext.webapp import template

WIKI_BASE = 'http://en.wikipedia.org/w/api.php'
BING_BASE = 'https://api.datamarket.azure.com/Bing/Search/v1/News'
REDDIT_BASE = 'http://www.reddit.com/api/'

class MainHandler(webapp2.RequestHandler):
    #Handle HTTP GET
    def get(self):
        self.response.write(users.get_current_user())
        self.response.write(wikiHome + "?format=json&action=query&titles=Main%20Page&prop=revisions&rvprop=content")
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        url = users.create_logout_url(self.request.uri)
        url_linktext = 'Logout'
        template_values = {'greetings': 'Hello',
        'url': url,
        'url_linktext': url_linktext,
        }
        self.response.out.write(template.render(path, template_values))
    #Handle HTTP POST
    def post(self):
        self.response.write('I got a post!')

class IndexHandler(webapp2.RequestHandler):
    #Handle HTTP GET    
    def get(self):
        self.response.write('Hello Index')\
        
#I need a handler for each type of incoming request.
app = webapp2.WSGIApplication([('/', MainHandler),('/index', IndexHandler)], debug=True)