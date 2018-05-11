import httplib2
import json

def getGeocodeLocation(inputString):
	google_api_key = "AIzaSyBEJ6VAb2eZ3_uehWlSeok_0whITsfaPlo"
	locationString = inputString.replace(" ", "+")
	url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))

	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	longitude = result['results'][0]['geometry']['location']['lng']
	latitude = result['results'][0]['geometry']['location']['lat']
	return (longitude, latitude)
