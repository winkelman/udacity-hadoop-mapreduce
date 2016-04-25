#!/usr/bin/python

import sys, csv

oldKey = None
count = 0
tag_counts = []

for line in sys.stdin:

    data = line.strip().split("\t")

    if len(data) != 1:
    	continue

    else:

    	thisKey = data[0].strip('"') # strips the double quotes on the input

    	# if we are at a new tag and it's not the 1st
    	if oldKey and thisKey != oldKey:

    		# add old tag and count to top tags list
    		tag_counts.append((oldKey, count))

    		# reset count for new tag
    		count = 1

    	# we are not at a new tag
    	else:
    		count += 1

    	oldKey = thisKey

# for the last post id since it didn't have a chance to print
if oldKey != None:
	tag_counts.append((oldKey, count))


# output top x tags
top_x_tags = sorted(tag_counts, key=lambda x: x[1], reverse=True)[0:10] # slice this list depending upon 'x'
for tag in top_x_tags:
    print "{0}\t{1}".format(tag[0], tag[1])