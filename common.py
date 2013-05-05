import sys

import urllib
import urllib2
import base64
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
user_agent = 'WhatHappend/1.0 +http://whathappened.appengine.com/ - starwalkerx18@gmail.com'
bing_account_key ='+vx7TXJXFsp1JxM8mEtY6FgeuRYhI5L5NVsq0crQ1Hc'
def GET(url):
    response = ""
    print url
    url = urllib.quote_plus(url,":/?=&")
    print url
    request = urllib2.Request(url)
    request.add_header('User-Agent', user_agent)
    request.add_header("Authorization", " Basic " + base64.b64encode(bing_account_key + ":" + bing_account_key))
    if (url != None):  
        try:
            print request.get_header("Authorization")
            response = urllib2.urlopen(request)
            response = response.read()
        except urllib2.HTTPError, e:
            sys.stderr.write("HTTP Error: %s %s"%(e.code,e.reason))
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
            request = urllib2.Request(query, params)
            request.add_header('User-Agent', user_agent)
            
            print request.get_full_url()

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

#print GET('http://api.bing.net/json.aspx?Appid=%2Bvx7TXJXFsp1JxM8mEtY6FgeuRYhI5L5NVsq0crQ1Hc&sources=image&query=xbox')   
print GET('https://api.datamarket.azure.com/Bing/Search/v1/RelatedSearch?Query=%27xbox%27')   
#print POST("http://www.google.com",{'test':'test'})