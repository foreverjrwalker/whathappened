#!/usr/bin/env python

import webapp2
import os
import common
import calendar_maker
import pprint
import time
import urllib

from google.appengine.api import users
from google.appengine.ext.webapp import template

import REST_wiki
import REST_bing
import REST_google
import REST_pdf

WIKI_BASE = 'http://en.wikipedia.org/w/api.php'
BING_BASE = 'https://api.datamarket.azure.com/Bing/Search/v1/News'
REDDIT_BASE = 'http://www.reddit.com/api/'

NUM_SEARCHES = 2

month_list = ['January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'] 

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
        self.response.write(REST_bing.getRelatedSearchWordsInJSON(self.request.get('query')))

class GoogleHandler(webapp2.RequestHandler):
    # Handle HTTP GET    
    print "Made it here"
    def post(self):
        self.response.write('Hello Post!')
        
class CalendarHandler(webapp2.RequestHandler):
    # Handle HTTP GET    
    print "Made it here"
    def get(self):
        query = self.request.get('query')
        date = self.request.get('date')
        date = common.splitDate(date)
        year = date[0]
        month = date[1]
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
        
        self.response.write(whatHappened(self.request.get('query'), self.request.get('date')))
    def post(self):
        self.response.write(whatHappened(self.request.get('query'), self.request.get('date')))
                
class WhatHappenedHandler(webapp2.RequestHandler):
    def get(self):
        output = whatHappened(self.request.get('query'), self.request.get('date'))
        self.response.out.write(output)
    # Handle HTTP POST
    
    def post(self):
        if (self.request.get('pdf') == 'on'):
            output = whatHappened(self.request.get('query'), self.request.get('date'))      
            self.response.headers['Content-Type'] = "application/pdf"
            self.response.write(common.POST('http://do.convertapi.com/web2pdf',{'curl':output}))
        else:
            output = whatHappened(self.request.get('query'), self.request.get('date'))      
            self.response.write(output)

def whatHappened(query, date):
    
    related_vals =  REST_bing.getRelatedSearchWords(query)
    search_values = []
    times_searched = 0
    found_vals = []
    while len(search_values) < NUM_SEARCHES:
        if (times_searched >= len(related_vals)):
            break
        else:
            term = related_vals[times_searched]
            results = REST_google.queryGoogle(term, date)
            if (len(results) > 0):
                found_vals.append(term)
                search_values.append(results)                    
            else:
                related_vals.remove(term)
            times_searched += 1
#     for i in range(NUM_SEARCHES):
#         if (i > len(related_vals)):
#             break
#         results = REST_google.queryGoogle(related_vals[i], date)
#         if (len(results) > 0):
#             search_values.append(results)    
#     
    date = common.splitDate(date)
    year = date[0]
    month = date[1]
    day = date[2]
    
    #date_text = REST_wiki.getArticleAbout("%s_%s")%(month_list[month],year)
    pprint.pprint(search_values)
    if len(search_values) > 0:
        returnval = calendar_maker.getCal(year,month,day, search_values, found_vals, NUM_SEARCHES, query)
    else: 
        returnval = "<html><body><h1>No Search Results Found</h1><br><h3>(Obviously nothing happened related to %s in %s of %s... ;-))</h3></body></html>"%(query,month_list[int(month)],year)
    return returnval
        
def parseDateText(dateText):
    return "True"
        
app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/google', GoogleHandler),
                               ('/calendar', CalendarHandler),
                               ('/bing', BingHandler),
                               ('/wiki', WikiHandler),
                               ('/wh', WhatHappenedHandler),
                               ('/test', TestHandler)
                               ], debug=True)
