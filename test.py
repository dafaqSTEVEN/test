import json
import requests
import time
 
localtime = time.asctime( time.localtime(time.time()) )
url = 'https://api.data.gov.hk/v1/carpark-info-vacancy'
r=requests.get(url = url)
print('HTML REQUEST STATUS : ' + str(r.status_code))
data = r.json()
for i in range (len(data['results'])):
	x = str(data["results"][i]['park_Id'])
	print(str(i+1) + ' : '+'Your Park Id is ' + str(x))
	y = str(data["results"][i]['displayAddress'])
	print('Address is : ' + str(y))
	z = str(data["results"][i]['contactNo'])
	print('Contact number is : ' + str(z))
	f = open("data.txt", "a")
	f.write(localtime + ' PARK_ID: ' + x + '\n')
	f.write(localtime + ' ADDRESS: ' +  y + '\n')
	f.write(localtime + ' CONTACT_NO: ' +  z + '\n')
	f.write('----------------------------------------\n')

