#!/usr/local/bin/python

# read in each line in /etc/passwd and parse it into a human readable form
# extra option - run with username to get results for just that user

import sys


file = open("/etc/passwd", "r")
for line in file:
	if (line[0] == "#"): continue

	if len(sys.argv) > 1:
		username = sys.argv[1]
	else:
		username = None

	thisline = line.split(":")
	if (username is not None and thisline[0] != username): continue

	print "Username: %s" % thisline[0]
	if (thisline[1] == "*"):
		print "Password shadowed"
	else:
		print "Password: %s" % thisline[1]
	print "UID: %s" % thisline[2]
	print "GID: %s" % thisline[3]
	print "Name: %s" % thisline[4]
	print "Home Directory: %s" % thisline[5]
	print "Shell: %s" % thisline[6]
