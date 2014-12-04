# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break
            
            fields = line.split(",")
            entry = {}
        
            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()
            
            data.append(entry)
            counter += 1
            
    print data

#parse_file(DATAFILE)



import os
import pprint
import csv

def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile,'rb') as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
    print data

#parse_csv(DATAFILE)






#!/usr/bin/env python
"""
Your task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. You should extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
You can use the csv modules "reader" method to get data in such format.
Another useful method is next() - to get the next line from the iterator.
You should only change the parse_file function.
"""
import csv
import os

DATADIR = ""
DATAFILE = "745090.csv"


def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
    # Do not change the line below
        text = csv.reader(f,delimiter=',', quotechar='"')
        data = next(text)
        name = data[1]
        next(text)
        data = list(text)
     
    return (name, data)






