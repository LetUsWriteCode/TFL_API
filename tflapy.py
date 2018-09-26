import requests
import json
import pprint

class tflapy(object):
	def __init__(self, app_id = None, app_key = None):
		"""
		app_id is your personal application ID
		app_key is the application Key.
		Both are optional but given during registration with TFL
		"""

	def _make_request(self, endpoint):
		"""
		Makes the actual GET request and returns the
		data in JSON format
		"""
		
		api = 'https://api.tfl.gov.uk'
		apiurl = api + endpoint

		req = requests.get(apiurl)

		if req.status_code == 200:
			data = req.json()
			return data
		else:
			error = 'Error: API Call not valid. Address Called: {}'.format(apiurl)
			print(error)

	def getAllStatus(self, mode):
		"""
		Gets the status of all the current lines
		DON'T put in Bus. It will get all the Buses running in London.
		"""
		endpoint = '/line/Mode/{}/Status'.format(mode)
		return self._make_request(endpoint)

d = tflapy()
pprint.pprint(d.getAllStatus('tube'))