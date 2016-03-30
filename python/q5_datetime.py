from datetime import datetime

####a) 

date_start = '01-02-2013'    
date_stop = '07-28-2015'

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m-%d-%Y")
    d2 = datetime.strptime(d2, "%m-%d-%Y")
    return abs((d2 - d1).days)
    
print days_between(date_start,date_stop)

####b)  
date_start = '12312013'  
date_stop = '05282015'

def convert_to_date(d1,d2):
	d1 = d1[0:2] + '-' + d1[2:4] + '-' + d1[4:9]
	d2 = d2[0:2] + '-' + d2[2:4] + '-' + d2[4:9]
	d1 = datetime.strptime(d1, "%m-%d-%Y")
	d2 = datetime.strptime(d2, "%m-%d-%Y")
	print abs((d2 - d1).days)    

convert_to_date(date_start,date_stop)

####c)  

from datetime import datetime

d1 = '15-Jan-1994'      
d2 = '14-Jul-2015'
d1 = datetime.strptime(d1, "%d-%b-%Y")
d2 = datetime.strptime(d2, "%d-%b-%Y")
print abs((d2 - d1).days)
