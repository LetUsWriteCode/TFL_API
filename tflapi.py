import requests
import json
import pprint


apiBase = 'https://api.tfl.gov.uk'
serviceAll = '/line/Mode/[]/Status'
serviceSpecify = '/Line/[]/Status'
arrival = '/StopPoint/[]/Arrivals'
searchStop = '/StopPoint/Search/[]'
searchStopMode = '?modes=[]'

## Check the status of all Tube and DLR services. Bus will return all modes
apiURL = apiBase + serviceAll
apiURL = apiURL.replace('[]','tube,dlr')

## Check the status of specified lines
apiURL = apiBase + serviceSpecify
apiURL = apiURL.replace('[]','circle%2C%20district')

# Check the arrivals for the bus stop nearby
stopid = '490003137X'

apiURL = apiBase + arrival
apiURL = apiURL.replace('[]',stopid)


## Search for StopPoint by name or 5 Digit Bus Stop Code
searchString = 'South Ealing'
searchString = searchString.replace(' ','%20')
searchStop = searchStop.replace('[]',searchString)
searchStopMode = searchStopMode.replace('[]','tube')

apiURL = apiBase + searchStop + searchStopMode

# Call the API and return JSON data
req = requests.get(apiURL)
data = req.json()

#Set the stop point for the station returned
stopPoint = data['matches'][0]['id']

# Recall the API to find arrivals
apiURL = apiBase + arrival
apiURL = apiURL.replace('[]',stopPoint)

req = requests.get(apiURL)
data = req.json()

for svc in data:
	direction = svc['platformName']
	if direction.find('Eastbound') != -1:
		pprint.pprint(svc)
