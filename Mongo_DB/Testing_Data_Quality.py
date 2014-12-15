#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then
clean it up. In the first exercise we want you to audit the datatypes that can be found in some 
particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a set of the datatypes
that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = {}

    for col in fields:
        fieldtypes[col] = set()
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "dbpedia" in row["URI"]:
                    if row[col]== "NULL" or row[col] == "":
                        fieldtypes[col].add(type(None))
                    elif row[col].startswith("{"):
                        fieldtypes[col].add(type([]))
                    elif is_number(row[col]):
                        if float(row[col]).is_integer():
                            fieldtypes[col].add(type(1.1))
                        else:
                            fieldtypes[col].add(type(1))
                    else:
                        fieldtypes[col].add(type("string"))


    return fieldtypes


def is_number(s): 
    try:
        float(s)
        return True
    except ValueError:
        return False





#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.

If you look at the full city data, you will notice that there are couple of values that seem to provide
the same information in different formats: "point" seems to be the combination of "wgs84_pos#lat" and "wgs84_pos#long".
However we do not know if that is the case and should check if they are equivalent.

Finish the function check_loc(). It will recieve 3 strings, first will be the combined value of "point" and then the
"wgs84_pos#" values separately. You have to extract the lat and long values from the "point" and compare
to the "wgs84_pos# values and return True or False.

Note that you do not have to fix the values, just determine if they are consistent. To fix them in this case
you would need more information. Feel free to discuss possible strategies for fixing this on the discussion forum.

The rest of the code is just an example on how this function can be used.
Changes to "process_file" function will not be take into account.
"""
import csv
import pprint

CITIES = 'cities.csv'


def check_loc(point, lat, longi):
    point = point.split(' ')
    if (float(lat) == float(point[0])) and (float(longi) == float(point[1])):
        return True
    else:
        return False
    
        
    print point, type(point)
    print lat
    print longi


def process_file(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #skipping the extra matadata
        for i in range(3):
            l = reader.next()
        # processing file
        for line in reader:
            # calling your function to check the location
            result = check_loc(line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
            if not result:
                print "{}: {} != {} {}".format(line["name"], line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
            data.append(line)

    return data
