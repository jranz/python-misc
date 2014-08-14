#!/usr/bin/python

##### Authors: Joseph Ranzenbach
##### Date:   8/13/2014
##### Input: CSV of API request URLs. Each API request URL is on a single line.
##### Output: Tab-separated file containing the API request URL, the HTTP response code (if not 200), 
############# and the corresponding error notification from the HTTP header.

import sys
import csv
import os
import urllib2
from urllib2 import URLError, HTTPError

urls="/Users/joey/Desktop/test.csv"
urls_out="/Users/joey/Desktop/url_test_out.csv"

start_urls = []
lines = open(urls).read().splitlines()
for url in lines:
	start_urls.append(url)


f = open(urls_out,'w')

# print len(start_urls)
# print start_urls[0]

for url in start_urls:
	try:
		result = urllib2.urlopen(url)
		# print result.read()
	# except URLError, e:
	# 	print e.code
	# 	print e.reason
	# 	print e.response
	# 	print e.read
	except HTTPError, e:
		# print e.code
		# print e.read()
		f.write(url + '\t'+ str(e.code) + '\t' + e.read() + '\n') # python will convert \n to os.linesep
		# print 


f.close()
		
