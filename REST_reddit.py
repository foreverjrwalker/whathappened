import urllib
import urllib2
import common

REDDIT_BASE = 'http://www.reddit.com/api/'

def printhello():
    print "Hello world!"
    
def getArticlesAbout(query):
    url = REDDIT_BASE + "v1/me.json"
 
    return common.GET(url)


print getArticlesAbout("")