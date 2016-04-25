#!/usr/bin/python

import sys, csv
from collections import Counter

# counter creates a hash (dictionary) counting the number of occurences for each value in a list
# we return all values from a list that have the maximum amount for that list (accounts for ties)
def getMode(some_list):
	counter = Counter(some_list)
	max_count = max(counter.values())
	mode = [number for number, count in counter.items() if count == max_count]
	return mode


oldKey = None
hours = []


for line in sys.stdin:

    data = line.strip().split("\t")

    if len(data) != 2:
    	continue

    else:

    	thisKey = data[0].strip('"') # strips the double quotes on the input
    	thisHour = data[1].strip('"')
    	
    	if oldKey and thisKey != oldKey:
			mostHour = getMode(hours)
			hours = [thisHour]
			for tied_hour in mostHour:
				# note that mostHour can be just 1 element
				print "{0}\t{1}".format(oldKey, tied_hour)

    	else:
    		hours.append(thisHour)

    	oldKey = thisKey


if oldKey != None:
	mostHour = getMode(hours)
	for tied_hour in mostHour:
		print "{0}\t{1}".format(oldKey, tied_hour)