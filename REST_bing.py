import REST_wiki
import urllib2
import urllib
import common
import json
import pprint

BING_BASE = 'https://api.datamarket.azure.com/Bing/Search/v1/RelatedSearch?Query='
BING_JSON = '&$format=json'
bing_account_key ='+vx7TXJXFsp1JxM8mEtY6FgeuRYhI5L5NVsq0crQ1Hc'

def getRelatedSearchWords(query):
    urlquery = urllib.quote_plus("'" + query + "'")   
    server_response = common.GET_raw(BING_BASE + urlquery + BING_JSON, bing_account_key)
    jo = json.load(server_response)
    obj_list = jo['d']['results']
    myTitles = [query]
    for item in obj_list:
        myTitles.append(item['Title'])
    return myTitles
    
