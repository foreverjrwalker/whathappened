import sys

import urllib
import urllib2
from google.appengine.api import urlfetch

#>>> payload = {'key1': 'value1', 'key2': 'value2'}
#>>> r = requests.get("http://httpbin.org/get", params=payload)

# def GET(url,payload={}):
#     response = ""
#      
#     print "Searching for " + url
#   
#     try:
#         response = requests.get(url, params=payload)
#         response.raise_for_status()
#             
#     except requests.exceptions.HTTPError, e:
#         sys.stderr.write("HTTP Error: %s"%(e.message))
#     except requests.exceptions.ConnectionError, e:
#         sys.stderr.write("Connection Error:" + e.message)
#     except requests.exceptions.InvalidURL, e:
#         sys.stderr.write("Invalid URL:" + e.message)
#     except Exception, e:
#         sys.stderr.write("Unknown Exception: " + e.message)
#     return response
#  
# def POST(query, params={}):
#     response = ""
#   
#     print "Searching for " + url
#        
#     try:
#         response = requests.post(url, data=payload)
#         response.raise_for_status()
#         
#     except requests.exceptions.HTTPError, e:
#         sys.stderr.write("HTTP Error: %s"%(e.message))
#     except requests.exceptions.ConnectionError, e:
#         sys.stderr.write("Connection Error:" + e.message)
#     except requests.exceptions.InvalidURL, e:
#         sys.stderr.write("Invalid URL:" + e.message)
#     except Exception, e:
#         sys.stderr.write("Unknown Exception: " + e.message)             
#     return response


def GET(url):
    response = ""
     
    print "Searching for " + url
    if (url != None):  
        try:
            #response = urllib2.urlopen(url).read()
            result = urlfetch.fetch(url)
            #jsondata = json.loads(result.content)
        except urllib2.HTTPError, e:
            sys.stderr.write("HTTP Error: %s %s"%(e.strerror,e.reason))
        except urllib2.URLError, e:
            sys.stderr.write("URL Error:" + e.message)
        except Exception, e:
            sys.stderr.write("Unknown Exception: " + e.message)
             
    return response
 
def POST(query, params):
    response = ""
     
    if (params != None):
        params = urllib.urlencode(params)    
        try:
            response = urllib2.urlopen(query, params).read()
        except urllib2.HTTPError, e:
            sys.stderr.write("HTTP Error: " + e.message)
        except urllib2.URLError, e:
            sys.stderr.write("URL Error:" + e.message)
        except Exception, e:
            sys.stderr.write("Unknown Exception: " + e.message)
             
    return response
