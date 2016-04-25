#!/usr/bin/python

import sys, csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next() #skip header

for line in reader:

    if len(line) != 19:
        continue

    node_id = line[0]
    author_id = line[3]
    parent_id = line[7]

    # we output 2 things; id of the original post, and author id of the question/answer/comment

    # if it has a parent id, assign post id and post type
    if parent_id == '\N':
    	post_id = node_id
    else:
    	post_id = parent_id
    
    writer.writerow([post_id, author_id]) # this double quotes the output
    #print "{0}\t{1}".format(author_id, time)
