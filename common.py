import sys

import urllib
import urllib2
import base64

user_agent = 'WhatHappened/1.0 +http://whathappened.appengine.com/ - starwalkerx18@gmail.com'

def GET(url, authorization_key=None):
    response = ""
    #url = urllib.quote_plus(url,":/?=&")
    request = urllib2.Request(url)
    request.add_header('User-Agent', user_agent)
    if (authorization_key):
        base64string = base64.encodestring('%s:%s' % (authorization_key, authorization_key)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)   
    if (url != None):  
        try:
            response = urllib2.urlopen(request)
            response = response.read()
        except urllib2.HTTPError, e:
            sys.stderr.write("HTTP Error: %s %s"%(e.code,e.reason))
        except urllib2.URLError, e:
            sys.stderr.write("URL Error:" + e.message)
        except Exception, e:
            sys.stderr.write("Unknown Exception: " + e.message)
    return response

def GET_raw(url, authorization_key=None):
    response = ""
    #url = urllib.quote_plus(url,":/?=&")
    request = urllib2.Request(url)
    request.add_header('User-Agent', user_agent)
    if (authorization_key):
        base64string = base64.encodestring('%s:%s' % (authorization_key, authorization_key)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)   
    if (url != None):  
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            sys.stderr.write("HTTP Error: %s %s"%(e.code,e.reason))
        except urllib2.URLError, e:
            sys.stderr.write("URL Error:" + e.message)
        except Exception, e:
            sys.stderr.write("Unknown Exception: " + e.message)
    return response
  
def POST(query, params):
    request = urllib2.Request(query)
    response = ""
    
    if (params != None):
        params = request.add_data(urllib.urlencode(params))    
        try:
            
            request.add_header('User-Agent', user_agent)
            response = urllib2.urlopen(request).read()

        except urllib2.HTTPError, e:
            sys.stderr.write("HTTP Error: %s %s"%(e.code,e.reason))
        except urllib2.URLError, e:
            sys.stderr.write("URL Error:" + e.message)
        except Exception, e:
            sys.stderr.write("Unknown Exception: " + e.message)
    else:
        print "Invalid Arguments"    
    return response

def splitDate(date):
    retVal = date.split('-')
    if len(retVal) < 3:
        retVal = ["Invalid Date"]
    return retVal

