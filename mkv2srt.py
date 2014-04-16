#!/usr/local/bin/python
#
# Script to rip srt/ssa subtitles out of .mkv files for use with my samsung TV and serviio on FreeBSD
# Usage: scriptname.py streamnumber [filename.mkv]
# If filename isn't specified all .mkv in the current directory will be converted
# Try ffmpeg -i filename to determine stream number you're after
#

import glob, re, sys, os
from subprocess import call

ffmpeg = '/usr/local/bin/ffmpeg'

def getcmd(i):
	srtfile = re.sub(r".mkv", ".srt", i)
	return [ffmpeg, '-i', i, '-vn', '-an', '-codec:s:0.%s' % (str(sys.argv[1])), 'srt', srtfile] 

if len(sys.argv) < 2:
	print "usage: %s stream [filename]\ntry: 'ffmpeg -i filename' to determine srt stream number" % os.path.basename(__file__) 
	sys.exit(0)

if len(sys.argv) < 3:
	mkvs = glob.glob("*.mkv")
	for i in mkvs:
		call(getcmd(i))
elif len(sys.argv) == 3:
	i = sys.argv[2]
	srtfile = re.sub(r".mkv", ".srt", i)
	call(getcmd(i))

