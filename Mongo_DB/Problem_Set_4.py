#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with another type of infobox data, audit it, clean it, 
come up with a data model, insert it into a MongoDB and then run some queries against your database.
The set contains data about Arachnid class.
Your task in this exercise is to parse the file, process only the fields that are listed in the
FIELDS dictionary as keys, and return a dictionary of cleaned values. 

The following things should be done:
- keys of the dictionary changed according to the mapping in FIELDS dictionary
- trim out redundant description in parenthesis from the 'rdf-schema#label' field, like "(spider)"
- if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
- if a value of a field is "NULL", convert it to None
- if there is a value in 'synonym', it should be converted to an array (list)
  by stripping the "{}" characters and splitting the string on "|". Rest of the cleanup is up to you,
  eg removing "*" prefixes etc
- strip leading and ending whitespace from all fields, if there is any
- the output structure should be as follows:
{ 'label': 'Argiope',
  'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
  'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
  'name': 'Argiope',
  'synonym': ["One", "Two"],
  'classification': {
                    'family': 'Orb-weaver spider',
                    'class': 'Arachnid',
                    'phylum': 'Arthropod',
                    'order': 'Spider',
                    'kingdom': 'Animal',
                    'genus': None
                    }
}
"""
import codecs
import csv
import json
import pprint
import re
import string

DATAFILE = 'arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'URI': 'uri',
         'rdf-schema#comment': 'description',
         'synonym': 'synonym',
         'name': 'name',
         'family_label': 'family',
         'class_label': 'class',
         'phylum_label': 'phylum',
         'order_label': 'order',
         'kingdom_label': 'kingdom',
         'genus_label': 'genus'}


def process_file(filename, fields):
    classification_list = ['family', 'class', 'phylum','order','kingdom', 'genus']
    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()
            
        for line in reader:
            new_dict = {}
            new_dict['classification'] = {}
            for field in fields:
                line[field] = line[field].strip()
                if fields[field] == "label":
                    # delete work inside parentheses in "rdf-schema#label"
                    line[field]=re.sub('\([^)]*\)','', line[field]).strip()
                    
                if fields[field] == 'name':
                    #if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
                    if (line[field]=='NULL') or (re.search('\W', line[field]) != None):
                        line[field] = line["rdf-schema#label"]
                # if a value of a field is "NULL", convert it to None
                if line[field] == "NULL":
                    line[field] = None
                #if there is a value in 'synonym', it should be converted to an array (list)
                if fields[field] == 'synonym':
                    if line[field] != None:
                        syn_list = []
                        for i in line[field].split('|'):
                            syn_list.append(i.strip("{} *"))
                        line[field] = syn_list
                if fields[field] in classification_list:
                    new_dict['classification'][fields[field]] = line[field]
                else:
                    new_dict[fields[field]] = line[field]
            data.append(new_dict)
    return data


def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return [v]




import json

def insert_data(data, db):
    
    for a in data:
        db.arachnid.insert(a)
    # Your code here. Insert the data into a collection 'arachnid'




if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    with open('arachnid.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print db.arachnid.find_one()
        
        
        
        
        
        
        

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with another type of infobox data, audit it, clean it, 
come up with a data model, insert it into a MongoDB and then run some queries against your database.
The set contains data about Arachnid class.

The data is already in the database. But you have been given a task to also include 'binomialAuthority'
information in the data, so you have to go through the data and update the existing entries.

The following things should be done in the function add_field:
- process the csv file and extract 2 fields - 'rdf-schema#label' and 'binomialAuthority_label'
- clean up the 'rdf-schema#label' same way as in the first exercise - removing redundant "(spider)" suffixes
- return a dictionary, with 'label' being the key, and 'binomialAuthority_label' the value
- if 'binomialAuthority_label' is "NULL", skip the item

The following should be done in the function update_db:
- query the database by using the field 'label'
- update the data, by adding a new item under 'classification' with a key 'binomialAuthority'


The resulting data should look like this:
- the output structure should be as follows:
{ 'label': 'Argiope',
  'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
  'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
  'name': 'Argiope',
  'synonym': ["One", "Two"],
  'classification': {
                    'binomialAuthority': None,
                    'family': 'Orb-weaver spider',
                    'class': 'Arachnid',
                    'phylum': 'Arthropod',
                    'order': 'Spider',
                    'kingdom': 'Animal',
                    'genus': None
                    }
}
"""
import codecs
import csv
import json
import pprint
import re

DATAFILE = 'arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'binomialAuthority_label': 'binomialAuthority'}


def add_field(filename, fields):
 
    process_fields = fields.keys()
    data = {}
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()
        for line in reader:
            # iterate over all keys in line to find proper value
            for key in line.keys():
                if key in process_fields:
                    #assign key to new key if label
                    value = None
                    if FIELDS[key] == 'label':
                        new_key = re.sub('\([^)]*\)','', line[key]).strip()
                    else:
                        if line[key] != 'NULL':
                            value = binominal_split(line[key])
                       
                    data[new_key] = value
 
 
 
    return data

 
def binominal_split(data):
 
    output = data
    if data.startswith('{'):
        output = data[1:-1].split('|')
    return output
 
def update_db(data, db):
 
    for key in data.keys():
        db.arachnid.update({'label' : key}, {'$set' : {'classification.binomialAuthority' : data[key]}})
 

        
        
        
        
        
        
        