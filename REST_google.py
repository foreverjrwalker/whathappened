import pprint, common, time, urllib

from apiclient.discovery import build

def getDateRange(date):
    date = common.splitDate(date)
    year = int(date[0])
    month = int(date[1])
    day =   int(date[2])
    a = (14 - month)//12
    y = year + 4800 - a
    m = month + 12*a - 3
    
    starttime = 1 + ((153*m + 2)//5) + 365*y + y//4 - y//100 + y//400 - 32045

    endday = 0
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        endday = 31
    elif (month == 2):
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 ==0):
            endday = 29
        else:
            endday = 28
    else:
        endday = 30
        
    endtime = endday + ((153*m + 2)//5) + 365*y + y//4 - y//100 + y//400 - 32045
    
    return [starttime, endtime]


def queryGoogle(query, date):
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  daterange = getDateRange(date)
  
  query = urllib.quote_plus(query)
  
  q = '"%s"daterange:%s-%s'%(query,daterange[0],daterange[1])   

  service = build("customsearch", "v1",
            developerKey="AIzaSyDcOcQeLrjcRBLtFI6kKj2pzvBproI3rMY")

  res = service.cse().list(
      q=q,
      cx='005816028885036704094:5w6o4vkz9j4',
      alt='json'
    ).execute()
    
    
  #If "items" isn't a valid search then return
  if not "items" in res:
      print "####################################################"
      pprint.pprint(res)
      print "FAIL"
      print "####################################################"
      return []
  
  result_list = res['items']
  return_list = [];
  for itemlist in result_list:
      cleanedupsnippet = cleanUpSnippet(itemlist['htmlSnippet'])
      if len(cleanedupsnippet) == 3:
          return_list.append([cleanedupsnippet,itemlist['title'],itemlist['formattedUrl']])
  
  return return_list
  #pprint.pprint(res)
  
def cleanUpSnippet(snippet):
    index = snippet.find("<")
    snipped = snippet[0:index].strip()
    snipped = snipped.split()
    for i in range(len(snipped)):
        snipped[i] = snipped[i].strip(',')
    return snipped
    
