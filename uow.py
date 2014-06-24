import urllib
import re

jobs = []
joburls = []
alljobs = []

link = "http://uow.employment.com.au/"
website = urllib.urlopen(link)
for line in website: 
	if line.find('/jobs/') != -1:
		result = re.search('"(.*)">(.*)<', line)
		print result.group(2) + " http://uow.employment.com.au" + result.group(1)
