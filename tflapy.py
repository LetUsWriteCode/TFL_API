import requests
import json
import pprint

api = 'https://api.tfl.gov.uk'

class tflapy(object):
	def __init__(self, app_id = None, app_key = None):
		"""
		app_id is your personal application ID
		app_key is the application Key.
		Both are optional but given during registration with TFL
		"""
		self.creds = ''
		if app_id != None:
			self.creds = '?app_id={}&app_key={}'.format(app_id, app_key)
		else:
			creds = None

	def _make_request(self, endpoint):
		"""
		Makes the actual GET request and returns the
		data in JSON format
		"""
		
		apiurl = api + endpoint + self.creds
		req = requests.get(apiurl)

		print(apiurl)

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

	def getLineStatus(self, line):
		"""
		Returns the status for specified lines
		Multiple lines can be defined with a comma
		"""
		endpoint = '/Line/{}/Status'.format(line)
		return self._make_request(endpoint)

	def checkArrival(self, stoppoint):
		"""
		Returns the arrival status for the specified stop point
		Stop Points can be found via the searchStopPoint
		"""
		endpoint = '/StopPoint/{}/Arrivals'.format(stoppoint)
		return self._make_request(endpoint)

	def searchStopPoint(self, search, mode):
		"""
		Performs a search for a stoppoint id using the search terms
		Will accept a common ane or the 5-Digit Countdown Bus Stop code
		"""
		endpoint = '/StopPoint/Search/{}'.format(search)
		return self._make_request(endpoint)
