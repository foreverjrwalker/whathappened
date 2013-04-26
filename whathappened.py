#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os

from google.appengine.api import users
from google.appengine.ext.webapp import template

wikiHome = 'http://en.wikipedia.org/w/api.php'

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
