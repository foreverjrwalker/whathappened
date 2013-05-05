import REST_wiki
import urllib2
import urllib

BING_BASE = 'https://api.datamarket.azure.com/Bing/Search/v1/RelatedSearch?Query='

def getRelatedSearchWords(query):
    #"Authorization: Basic " . base64_encode($accountKey . ":" . $accountKey
    print urllib.urlencode(BING_BASE + query)