import urllib
import urllib2
import common
import pprint
import json

wiki_base = 'http://en.wikipedia.org/w/api.php?format=json&action=query'

def printhello():
    print "Hello world!"
    
def getArticleAbout(query):
    query = urllib.quote_plus(query)   
    url = "http://en.wikipedia.org/w/api.php?action=parse&format=json&page=%s&prop=text&redirects"%query
    server_response = common.GET_raw(url)
    jo = json.load(server_response)
    text = jo['parse']['text']["*"]
    return pprint.pformat(text)

