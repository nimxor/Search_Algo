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

doc = {}

with open('where.json') as data_file:    
    fhand = json.load(data_file)
    for line in fhand :
    	title = line[0]['title']
    	star()
    	print title
    	web_list = []
    	star()
    	for data in line :
    		data = str(data).strip().split(':')
    		if data[0]=="{u'title'" :
    			continue
    		link = data[1]+data[2]
    		web_title = data[0][2:]
    		web_link = link[2:-1]
    		web_list.append([web_title,web_link])
    	doc[title]=web_list
    		
print doc    	
