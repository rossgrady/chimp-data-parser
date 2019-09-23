#!/usr/bin/env python3

# script to walk through a directory structure delivered by the mailchimp legal team
# and produce a single CSV of all of the mailing list info within that directory structure
#
# usage: request & receive a zipfile from mailchimp of all your data
#        unzip that zipfile into a directory
#        copy this file into the top level of that directory
#        e.g. when doing an ls on that directory, you should see something like this:
#
#        my-laptop$ ls -l
#        drwxr-xr-x@ 96 my-user  staff  3072 Sep 23 14:37 c6ae6992-692e-47a1-b920-5d028600db62
#        -rwxr-xr-x   1 my-user  staff  1845 Sep 23 14:41 science.py
#
#        execute science.py at the cmd line from within that directory (e.g.: ./science.py)
#
#        you should now have a CSV file in that same directory, for example:
#
#        my-laptop$ ls -l
#        drwxr-xr-x@ 96 my-user  staff    3072 Sep 23 14:37 c6ae6992-692e-47a1-b920-5d028600db62
#        -rw-r--r--   1 my-user  staff  235226 Sep 23 14:43 c6ae6992-692e-47a1-b920-5d028600db62.csv
#        -rwxr-xr-x   1 my-user  staff    2003 Sep 23 14:43 science.py
#
#        that's it, that's how it works. The CSV should have all the data.


import os
import csv
import sys

keysdict = {"ape_user":"ape_user","ape_list":"ape_list","ape_listemail":"ape_listemail"}
keyslist = []
datalist = []
counter = 0

for root, dirs, files in os.walk(u"."):
  path = root.split(os.sep)
  for file in files:
    if file == 'list.csv':
      tmpdatalist = {}
      with open(os.path.join(root, file), 'rt') as listfile:
        for line in listfile:
          line = line.rstrip()
          words = line.split(",")
          if(words[1] != ""):
            keysdict[words[0]] = words[1]
            tmpdatalist[words[0]] = words[1]
      with open(os.path.join(root, "campaigns","sends.csv"), 'rt') as sendsfile:
        reader = csv.DictReader(sendsfile)
        for row in reader:
          datalist.insert(counter,{"ape_user":path[2], "ape_list":path[3], "ape_listemail":path[4]})
          for key in tmpdatalist:
            datalist[counter][key] = tmpdatalist[key]
          for key in row:
            if(row[key] != ""):
              keysdict[key] = row[key]
              datalist[counter][key] = row[key]
          counter += 1
      
for keyword in keysdict:
  keyslist.append(keyword)
outfile = path[1]+".csv"
csvfile = open(outfile, 'w', newline='')
writer = csv.DictWriter(csvfile, fieldnames=keyslist)
writer.writeheader()
for entry in datalist:
  writer.writerow(entry)
csvfile.close()
