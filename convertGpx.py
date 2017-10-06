#!/usr/bin/python
""" Simple Utility for shifting GPX activity files in time.

Created to work around Strava's incorrect splitting of a multi-activity file imported from Garmin.
Ended up with overlapping and incorrect activities.

Will shift any time object in the following format
<time>2017-09-17T11:33:05Z</time>

"""

import sys
import re
from dateutil.parser import parse
from datetime import datetime 
from datetime import timedelta 

# time offset in minutes
time_offset = -130

# read in the file
gpx_in = './input.gpx'
input_file = open(gpx_in,'r')
gpx_out = './output.gpx'
output_file = open(gpx_out,'w')

# read line
for line in input_file.readlines():
	m = re.search('<time>(.*)</time>', line)
	if m != None:
		# convert m.group(0) to a date obj
		time = datetime.strptime(m.group(1), '%Y-%m-%dT%H:%M:%SZ')
		# shift it based on offset
		delta = timedelta(minutes=time_offset)
		new_time = time + delta
		# rewrap in <time></time>\n
		new_time_string = new_time.strftime('%Y-%m-%dT%H:%M:%SZ')
		line = '<time>'+new_time_string+'</time>\n'
	output_file.write(line)

input_file.close()
output_file.close()

