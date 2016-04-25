#!/usr/bin/python

import sys, csv

oldKey = None
questionLength = None
answerCount = 0
answerTotal = 0

for line in sys.stdin:

    data = line.strip().split("\t")

    if len(data) != 3:
    	continue

    else:

    	thisKey = data[0].strip('"') # strips the double quotes on the input
    	thisType = data[1].strip('"')
    	thisLength = int(data[2].strip('"')) # length needs to be an integer

    	# if we are at a new post id and it's not the 1st
    	if oldKey and thisKey != oldKey:

    		# calculate the average answer length, make sure we don't divide by 0
    		if answerCount == 0:
    			answerAvg = 0
    		else:
    			answerAvg = 1.0*answerTotal/answerCount

    		print "{0}\t{1}\t{2}".format(oldKey, questionLength, answerAvg) # output stats for that post id

    		# reset question length, answer count and answer total
    		questionLength = thisLength
    		answerCount, answerTotal = 0, 0

    	# we are not at a new post id
    	else:

    		# when it is the question post, set question length
    		if thisType == "1":
    			questionLength = thisLength

    		# when it is an answer post, add to answer stats
    		else:
				answerTotal += thisLength
				answerCount += 1

    	oldKey = thisKey

# for the last post id since it didn't have a chance to print
if oldKey != None:

	answerAvg = 0 if answerCount == 0 else (1.0*answerTotal/answerCount)
	print "{0}\t{1}\t{2}".format(oldKey, questionLength, answerAvg)