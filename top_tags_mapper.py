#!/usr/bin/python

import sys, csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next() #skip header

for line in reader:

    if len(line) != 19:
        continue

    tag_names = line[2]
    node_type = line[5]

    if node_type == "question":
        tag_list = tag_names.split()

        for tag in tag_list:
            writer.writerow([tag]) # this double quotes the output
            #print "{0}\t{1}".format(author_id, time)