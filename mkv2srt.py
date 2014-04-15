#!/usr/local/bin/python
# Script to rip srt/ssa subtitles out of .mkv files for use with my samsung TV and serviio on FreeBSD
# Usage: scriptname.py streamnumber
# Try ffmpeg -i filename to determine stream number you're after

import glob, re, sys, os
from subprocess import call

if len(sys.argv) < 2:
	print "usage: %s stream\ntry: 'ffmpeg -i filename' to determine srt stream number" % os.path.basename(__file__) 
	sys.exit(0)

mkvs = glob.glob("*.mkv")

for i in mkvs:
	srtfile = re.sub(r".mkv", ".srt", i)
	cmd = ['/usr/local/bin/ffmpeg', '-i', i, '-vn', '-an', '-codec:s:0.%s' % (str(sys.argv[1])), 'srt', srtfile] 
	print cmd
	call(cmd)
