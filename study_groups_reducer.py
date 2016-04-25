#!/usr/bin/python

import sys, csv

oldKey = None
count = 0
thread_participants = []

# note that the participants is not unique
# we want to count each time a user interacts in a thread to measure intensity

for line in sys.stdin:

    data = line.strip().split("\t")

    if len(data) != 2:
    	continue

    else:

    	thisKey = data[0].strip('"') # strips the double quotes on the input
        thisPerson = data[1].strip('"')

    	# if we are at a new thread and it's not the 1st
    	if oldKey and thisKey != oldKey:

    		# output thread id and all participants
            print "{0}\t{1}".format(oldKey, thread_participants)

    		# reset participants list to this person
            thread_participants = [thisPerson]

    	# we are not at a new thread
    	else:
    		thread_participants.append(thisPerson)

    	oldKey = thisKey

# for the last thread since it didn't have a chance to print
if oldKey != None:
	print "{0}\t{1}".format(oldKey, thread_participants)