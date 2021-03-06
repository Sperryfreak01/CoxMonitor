#Copywrite Matt Lovett 2015

from bs4 import BeautifulSoup
from requests import session
import sys
#import codecs
import time
from datetime import date
import notifications

#ENTER YOUR COX LOGIN INFORMATION BELOW
COX_username = ""
COX_password = ""


#ENTER PUSHOVER INFO TO GET RECIEVE PUSH NOTIFICATIONS
Pushover_user_token = ''
Pushover_app_token = ''

###########################################################################################################################3

limit = ''
usage = ''
remain = ''
d0 = date.today()
delta = ''

payload = {
    'onsuccess'   : 'https://myaccount.cox.net/internettools/datausage/usage.cox',
    'onfailure'   : 'http://www.cox.com/resaccount/orangecounty/sign-in.cox',
    'targetFN'    : 'COX.net',
    'emaildomain' : '@cox.net',
    'username'    : COX_username,
    'password'    : COX_password,
    'rememberme'  : 'on'
}

with session() as web:
    web.post('https://idm.east.cox.net/idm/coxnetlogin', data=payload)
    request = web.get('https://myaccount.cox.net/internettools/datausage/usage.cox')

    soup = BeautifulSoup(request.text, 'html5lib')
    x = 0
    for cols in soup.findAll('td')
        for cell in cols:
            if "GB" in cell:
                x = x + 1
                if x == 1:
                   limit = cell.strip()
                   print (limit)
                   print ('Monthly limit is ' + limit)
                elif x == 2:
                   usage = cell.strip()
                   print (usage)
                   print ('Current usage is ' +usage)
                elif x == 3:
                    remain = cell.strip()
                    print(remain)
                    print ('Remaining bandwidth is ' + remain)

    d1 = d0.replace(month = d0.month + 1, day = 04)
    print (d1)
    delta = d1 - d0
    print delta.days
    notifications.pushover(message=usage +' of the ' + limit + ' month limit has been used. ' + remain + ' remains for the next ' + str(delta.days) + ' days', 
			   token = Pushover_app_token, 
			   user = Pushover_user_token)





