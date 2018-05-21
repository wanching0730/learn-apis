import json
import httplib2
import sys
import codecs

sys.stdout = codecs.getwritter('utf8')(sys.stdout)
sys.stderr = codecs.getwritter('utf8')(sys.stderr)

foursquare_client_id = ""
foursquare_client_secret = ""
google_api_key = ""

def getGeoLocation(inputString):
	# replace space with '+' in url
	locationString = inputString.replace(" ", "+")
	url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
	h = httplib2.Http()
	result = json.loads(h.request(url, 'GET')[1])
	latitude = result['results'][0]['geometry']['location']['lat']
	longitude = result['results'][0]['geometry']['location']['lng']
	return (latitude, longitude)

# take a string representation of a location and cuisine type, geocode the location,
# and then pass in the latitude and longitude to Foursquare api
def findRestaurant(mealType, location):

	# get longitude and latitude of the location
	latitude, longitude = getGeocodeLocation(location)

	# use foursquare api to find nearby restaurant with longitude, latitude, mealtype
	# format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret, latitude, longitude, mealType))

	h = httplib2.Http()
	result = json.loads(h.request(url, 'GET')[1])

	if result['response']['venues']:
		# Take the first restaurant
		restaurant = result['response']['venues'][0]
		venue_id = restaurant['id']
		restaurant_name = restaurant['name']
		# an array of addresses
		restaurant_address = restaurant['location']['formattedAddress']
		address = ""
		for i in restaurant_address:
			address += i + " "
		restaurant_address = address

		# Get picture of the restaurant
		url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((venue_id, foursquare_client_id, foursquare_client_secret)))
		result = json.loads(h.request(url, 'GET')[1])

		if result['response']['photos']['items']:
			# Take first image
			firstpic = result['response']['photos']['items'][0]
			prefix = firstpic['prefix']
			suffix = firstpic['suffix']
			# can change 300x300 to original 
			imageURL = prefix + "300x300" + suffix
		else: 
			# if no image available, insert default iamge url
			imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"


		# return a dictionary containing restaurant name, address, image url
		restaurant_info = {'name': restaurant_name, 'address': restaurant_address, 'image': imageURL}
		print "Restaurant name: %s" % restaurant_info['name']
		print "Restaurant address: %s" % restaurant_info['address']
		print "Image: %s \n" % restaurantInfo['image']

		return restaurant_info

	else: 
	 	print "No restaurant found for %s" % location
	 	return "No restaurant found"


if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")