import re, datetime
import calendar
import pprint

def getCal(year, month, day, items_to_add, related_vals, NUM_SEARCHES, QueryTerm):
    
    calendar.setfirstweekday(6)
    
    year_list = ['January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'] 
     
    month = int(month)
    current_month = year_list[month - 1] 
    current_day = int(day) 
    current_yr = int(year) 
    
    html_page = ''' 
    
    <!DOCTYPE html> 
    <HTML > 
    <head > 
        <title >%s %s</title >''' % (current_month, current_yr)
    
    html_page += '''  
           <style type="text/css" > 
                html, body { margin: 0; padding: 0 } 
                body { background-color:#060; } 
                #container { margin: 3em auto 0 3em; padding-bottom: 3em; background-color: #fff; } 
                #month { border-collapse: collapse; margin-left: 2em; } 
                #month th, #month td { border: 1px solid #000; } 
                #month thead { background-color:#9c9; } 
                #month td { width: 7em; height: 7em; padding: .2em; vertical-align: top; overflow: auto; } 
                td .day { width: 7em; height: 6em; overflow:auto; margin-top: 0; } 
                #month tbody .weekend { background-color:#ded; } 
                #month tbody .next, #month tbody .previous { background-color:#ddd; } 
                .rtop { display:block; background:#060; } 
                .rtop * { display: block; height: 1px; overflow: hidden; background:#fff; } 
                .r1{margin: 0 0 0 5px} 
                .r2{margin: 0 0 0 3px} 
                .r3{margin: 0 0 0 2px} 
                .r4{margin: 0 0 0 1px; height: 2px} 
                #container h1 { margin: 0 0 .5em .5em; font: 2em Arial, Helvetica, sans-serif; color: #060; } 
                #month th { font: 1em bold Arial, Helvetica, sans-serif; } 
                p {margin-top: 0; } 
            </style > 
    </head > 
    
    <body > 
    
        <div id="container" > 
        <b class="rtop" ><b class="r1" ></b > <b class="r2" ></b ><b class="r3" ></b > <b class="r4" ></b ></b >''' 
    
    html_page += '<h1><b>What Happened</b> relating to <b> %s </b> during %s of %s? </h1 >' % (QueryTerm, current_month, current_yr)
    html_page += '<h2>Displaying results from the following search terms: '
    for item in related_vals:
        html_page += item + ", "
        
    html_page += ''' 
        </h2>
        <table id="month" > 
        <thead > 
        <tr > 
        <th class="weekend" >Sunday</th > 
        <th >Monday</th > 
        <th >Tuesday</th > 
        <th >Wednesday</th > 
        
        <th >Thursday</th > 
        <th >Friday</th > 
        <th class="weekend" >Saturday</th > 
        </tr > 
        </thead > 
        <tbody > 
    '''   
    month_list = calendar.monthcalendar(current_yr, month) 
    nweeks = len(month_list) 
    
    for w in range(0, nweeks): 
        week = month_list[w] 
        html_page += "<tr>" 
        for x in xrange(0, 7): 
            day = week[x] 
            
            if x == 0 or x == 6: 
                classtype = 'weekend' 
            else: 
                classtype = 'day' 
            if day == 0: 
                classtype = 'previous' 
                html_page += '<td class="%s"></td>' % (classtype) 
            elif day == current_day: 
                html_page += '<td class="%s"><strong>%s</strong></span><div class="%s"></div>' % (classtype, day, classtype)
                # insert day stuff here
                # day matches so include the important stuff
                for query in items_to_add:
                    for i2a in query:    
                        if day == int(i2a[0][1]):
                            html_page += "<a href=http://%s> %s </a><br>" % (i2a[2], i2a[1])
                # close table item
                html_page += '</td>'     
                

            else: 
                html_page += '<td class="%s">%s</span><div class="%s"></div>' % (classtype, day, classtype)
                for query in items_to_add:
                    for i2a in query:    
                        if day == int(i2a[0][1]):
                            html_page += "<a href=http://%s> %s </a><br>" % (i2a[2], i2a[1])
                html_page += '</td>'
                
                
        html_page += "</tr>" 
    
    html_page += ''' </tbody> 
    </table> 
    </div> 
    </body> 
    </html>'''

    return html_page
val = [[[u'Dec', u'23', u'2008'],
  u'Doctors Warn: Wii Puts 10 In Hospital a Week | Fox News',
  u'www.foxnews.com/story/0,2933,471364,00.html'],
 [[u'Dec', u'27', u'2008'],
  u'WeeP5 makes other Wiimote gun mods cry home to their mamas',
  u'www.engadget.com/.../weep5-makes-other-wiimote-gun-mods-cry-home-to- their-mamas/'],
 [[u'Dec', u'23', u'2008'],
  u'Wii blamed for ridiculous increase in British hospital visits - Engadget',
  u'www.engadget.com/.../wii-blamed-for-ridiculous-increase-in-british-hospital- visits/'],
 [[u'Dec', u'19', u'2008'],
  u'Wii-controlled robots made for combat - Technology & science ...',
  u'www.nbcnews.com/id/.../t/wii-controlled-robots-made-combat/'],
 [[u'Dec', u'19', u'2008'],
  u"Nintendo's 'Wii Music' Waits for Fans to Find It | Fox News",
  u'www.foxnews.com/.../nintendo-wii-music-waits-for-fans-to-find-it'],
 [[u'Dec', u'29', u'2008'],
  u'PS3 unable to hold its own against Wii, Xbox 360 this holiday season',
  u'www.engadget.com/.../ps3-unable-to-hold-its-own-against-wii-xbox-360-this -holiday-se/'],
 [[u'Dec', u'10', u'2008'],
  u'New Wii drives breaking modchips, hearts, legs - Engadget',
  u'www.engadget.com/.../new-wii-drives-breaking-modchips-hearts-legs/'],
 [[u'Dec', u'12', u'2008'],
  u"It's all about Nintendo as Wii, DS dominate November sales | Ars ...",
  u'arstechnica.com/.../its-all-about-nintendo-as-wii-ds-dominate-november-sales/'],
 [[u'Dec', u'18', u'2008'],
  u'Star Wars Wii mod realizes very few of our childhood dreams',
  u'www.engadget.com/.../star-wars-wii-mod-realizes-very-few-of-our-childhood -dreams/'],
 [[u'Dec', u'10', u'2008'],
  u'SwiitBoard: the sweeter way to get fit on the Wii - Engadget',
  u'www.engadget.com/.../swiitboard-the-sweeter-way-to-get-fit-on-the-wii/']]


if __name__ == "__main__": 
    print getCal("2008", "12", "1", val)
