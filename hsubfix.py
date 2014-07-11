#!/usr/local/bin/python
#
# Script to clean up srt subtitles ripped out of .mkv files for use with my samsung TV and serviio on FreeBSD
# Usage: scriptname.py [filename.srt]
# If the filename isn't specified all .srt files in the current directory will be processed 
#

import glob, re, argparse
from subprocess import call

vim = '/usr/local/bin/vim'
hsub = '/home/nick/scripts/hsubs.txt'


parser = argparse.ArgumentParser(description='Clean up HorribleSubs srt files for use on a Samsung TV.')
parser.add_argument('-f', '--file', help="source filename (srt) to clean up")
args = parser.parse_args()

def process(i):
	return [vim, '-s', hsub, i]

if args.file is None:
	srts = glob.glob("*.srt")
	if (len(srts) == 0):
		print "No .srt files in current directory"
	for i in srts:
		print process(i)
		#call(process(i))
else:
	call(process(args.file))
