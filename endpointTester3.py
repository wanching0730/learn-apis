import httplib2
import json
import sys

print("running endpoint tester...\n")
address = input("Please enter the address of the server you want, if not, default is http://localhost:5000: ")
if address == '':
	address = 'http://localhost:5000'

#making post request
print("making post request to /puppies...")
try:
	url = address + "/puppies?name=Fido&description=Playful+Little+Puppy"
	h = httplib2.Http()
	response, result = h.request(url, 'POST')
	obj = json.loads(result)
	puppyID = obj['Puppy']['id']
	if response['status'] != '200':
		raise Exception('Received an uncessful status code of  %s' % resp['status'])
except Exception as err:
	print("Test 1 failed: counld not make post request to web server")
	print(err.args)
	sys.exit()
else: 
	print("test 1 pass: successfully made post request to /puppies")

