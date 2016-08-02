import re
import os
import json
import codecs
import requests
import urllib
from bs4 import BeautifulSoup
from pprint import pprint

def star():
	rows,cols = os.popen('stty size','r').read().split()
	cols = int(cols)
	print( '\n' +  '*'*cols + '\n' )

with open('where.json') as data_file:    
    fhand = json.load(data_file)
    for line in fhand :
    	title = line[0]['title']
    	star()
    	print title
    	star()
    	for data in line :
    		data = str(data).strip().split(':')
    		if data[0]=="{u'title'" :
    			continue
    		data = str(data).split("u'")
    		print data
    	
