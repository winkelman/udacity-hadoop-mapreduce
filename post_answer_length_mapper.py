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
    body = line[4]
    node_type = line[5]
    parent_id = line[7]
    length = len(body)

    # we output 3 things: id of the original post, whether it is a question or answer, and length
    # for sorting purposes, we use a '1' for the question and '2' for the answer

    # assign a post id and number for post type
    if node_type == 'question':
    	post_id = node_id
    	post_type = 1
    else:
    	post_id = parent_id
    	post_type = 2

    # shorter but less pythonic way
    '''
    post_type = 1 if node_type == 'question' else 2
    post_id = node_id if node_type == 'question' else parent_id
    '''
    
    writer.writerow([post_id, post_type, length]) # this double quotes the output
    #print "{0}\t{1}".format(author_id, time)
