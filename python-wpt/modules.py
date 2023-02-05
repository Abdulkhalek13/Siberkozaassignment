# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Akz = Abdul khalek zouhori


# core modules available by default

import datetime
from datetime import date
import time
from time import time

# Pip modules
#from camelcase import camelcase





#today_Akz = datetime.date.today()
today_Akz = date.today()

#timestamp_Akz = time.time()
timestamp_Akz = time()

#camelcase
#c_Akz = camelcase
#print(c_Akz.hump('hello world'))

print(today_Akz)
print(timestamp_Akz)


# import costum module
import validator
from validator import validate_email

email_Akz = 'test.com'
if validate_email(email_Akz):
    print('email is valid')
else:
    print('email is bad')   
     









