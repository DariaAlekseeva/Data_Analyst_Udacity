#!/usr/bin/env python
"""
Your task is to complete the 'porsche_query' function and in particular the query
to find all autos where the manufacturer field matches "Porsche".
Please modify only 'porsche_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB and download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials at
the following link:
https://www.udacity.com/wiki/ud032
"""


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db


def porsche_query():
    # Please fill in the query to find all autos manuafactured by Porsche
    query = {"name":"Porsche Boxster"}
    return query


def find_porsche(db, query):
    return db.autos.find(query)






from autos import process_file


def insert_autos(infile, db):
    autos = process_file(infile)

    # Your code here. Insert the data in one command
    # autos will be a list of dictionaries, as in the example in the previous video
    # You have to insert data in a collection 'autos'
    for a in autos:
        db.autos.insert(a)

  
if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos('autos-small.csv', db)
    print db.autos.find_one()
    
    
    
    
    
    #!/usr/bin/env python
""" Your task is to write a query that will return all cities
that are founded in 21st century.
Please modify only 'range_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.
"""
from datetime import datetime
    
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


def range_query():
    # You can use datetime(year, month, day) to specify date in the query
    query = {'foundingDate': {"$gte":datetime(2000,12,31)}}
    return query


#!/usr/bin/env python
""" Your task is to write a query that will return all cars manufactured by "Ford Motor Company"
that are assembled in Germany, United Kingdom, or Japan.
Please modify only 'in_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.
"""

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


def in_query():
    # Write the query
    query = {"assembly" : {"$in":["Germany", "United Kingdom", "Japan"]}, "manufacturer":"Ford Motor Company"}
    
    return query





#!/usr/bin/env python
""" Your task is to write a query that will return all cars with width dimension greater than 2.5
Please modify only 'dot_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.
"""


def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


def dot_query():
    query = {"dimensions.width":{"$gt":2.5}}
    return query

