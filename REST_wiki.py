import urllib2
import common
wiki_base = 'http://en.wikipedia.org/w/api.php'

def printhello():
    print "Hello world!"
    
def getArticleAbout(query):
    url = "http://en.wikipedia.org/wiki/Special:ApiSandbox#action=parse&format=json&page=%s&prop=text"%query
    return common.GET(url)