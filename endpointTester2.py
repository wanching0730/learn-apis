import httplib2
import json
import sys

print "Running endpoint tester...\n"
address = raw_input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':")
if address == '':
	address = 'http://localhost:5000'

# Making GET Request
print "Making a GET request for puppies..."
try:
	url = address + "/puppies"
	h = httplib2.Http()
	response, result = h.request(url, 'GET')
	if response['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % response['status'])
except Exception as err:
	print "Test 1 FAILED: Could not make Get request to web server"
	print err.args
	sys.exit()
else: 
	print "Test 1 PASS: Success made get request to /puppies"