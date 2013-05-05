#!/usr/bin/env python

import webapp2
import os
import common

from google.appengine.api import users
from google.appengine.ext.webapp import template

import REST_reddit
import REST_wiki
import REST_bing


WIKI_BASE = 'http://en.wikipedia.org/w/api.php'
BING_BASE = 'https://api.datamarket.azure.com/Bing/Search/v1/News'
REDDIT_BASE = 'http://www.reddit.com/api/'

class MainHandler(webapp2.RequestHandler):
    # Handle HTTP GET
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        url = users.create_logout_url(self.request.uri)
        url_linktext = 'Logout'
        template_values = {'greetings': 'Hello',
        'url': url,
        'url_linktext': url_linktext,
        }
        self.response.out.write(template.render(path, template_values))
    # Handle HTTP POST
    def post(self):
        self.response.write('I got a post!')

class BingHandler(webapp2.RequestHandler):
    # Handle HTTP GET    
    print "Made it here"
    def post(self):
        self.response.write('Hello Post!')

class GoogleHandler(webapp2.RequestHandler):
    # Handle HTTP GET    
    print "Made it here"
    def post(self):
        self.response.write('Hello Post!')

class RedditHandler(webapp2.RequestHandler):
    # Handle HTTP GET    
    print "Made it here"
    def post(self):
        self.response.write('Hello Post!')
        
class WikiHandler(webapp2.RequestHandler):
    # Handle HTTP GET    
    print "Made it here"
    def post(self):
        query = self.request.get('query')
        date = self.request.get('date')
        date = common.splitDate(date)
        year = date[0]
        month = date[1]
#        result = REST_wiki.getArticleAbout(query, month, year)
#        self.response.write(result)
        self.response.write(query)  
        self.response.write("<br>")      
        self.response.write(year)
        self.response.write("<br>")      
        self.response.write(month)
        
class TestHandler(webapp2.RequestHandler):
    # Handle HTTP GET    
    print "Made it here"
    def get(self):
        
        self.response.write(common.GET(self.request.get('query')))
    def post(self):
        args = {'query' : ''}
        self.response.write(common.POST("http://google.com", args))
                
        
        
app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/reddit', RedditHandler),
                               ('/google', GoogleHandler),
                               ('/bing', BingHandler),
                               ('/wiki', WikiHandler),
                               ('/test', TestHandler)
                               ], debug=True)
