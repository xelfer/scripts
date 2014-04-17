#!/usr/local/bin/python
#
# Script to rip srt/ssa subtitles out of .mkv files for use with my samsung TV and serviio on FreeBSD
# Usage: scriptname.py [filename.mkv]
# If the filename isn't specified all .mkv files in the current directory will be processed 
# Developed with ffmpeg 2.1.1, you probably want that or higher if this doesn't work
#

import glob, re, argparse
from subprocess import call

ffmpeg = '/usr/local/bin/ffmpeg'

parser = argparse.ArgumentParser(description='Extract subtitles from mkv files.')
parser.add_argument('-f', '--file', help="source filename (mkv) to extract subtitle from")
args = parser.parse_args()

def process(i):
	return [ffmpeg, '-i', i, re.sub(r".mkv", ".srt", i)] 

if args.file is None:
	mkvs = glob.glob("*.mkv")
	if (len(mkvs) == 0):
		print "No .mkv files in current directory"
	for i in mkvs:
		call(process(i))
else:
	call(process(args.file))

