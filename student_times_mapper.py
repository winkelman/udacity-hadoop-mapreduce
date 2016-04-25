#!/usr/bin/python

import sys, csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next() #skip header

for line in reader:

    if len(line) != 19:
        continue

    author_id = line[3]
    time = line[8]
    # get the hour from the time field
    time = re.search(r"\s+\w+\:+", time).group()[1:3]
    
    writer.writerow((author_id, time)) # this double quotes are output
    #print "{0}\t{1}".format(author_id, time)
