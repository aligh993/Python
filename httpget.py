# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import requests
import datetime
url = "http://78.38.208.36:5000/index/"
s   = requests.Session()
start_time = datetime.datetime.now()
for x in range(0, 100):       
    myurl = url + str(x)
    r = s.get(myurl)
    response_content = r.content
    print (x, "\t", myurl, "\t", r.status_code)

print(datetime.datetime.now()-start_time)
