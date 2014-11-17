from pandas import *
import numpy

def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    baseball = pandas.read_csv(filename)
    value = numpy.mean(baseball['weight'])
    baseball['weight'] = baseball['weight'].fillna(value)
    
    #YOUR CODE GOES HERE

    return baseball





import json
import requests


# if __name__=="__main__":
#     url = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=8d38e993773dce11d41974fa178f8216&artist=Rihanna&album=Unapologetic&format=json'
#     data = requests.get(url).text
#     data = json.loads(data)
#     print type(data)
#     print data
#     data['artist']
  
import json
import requests
from pprint import pprint

def api_get_request(url):
    if __name__  == "__main__":
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
        url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=8d38e993773dce11d41974fa178f8216&format=json'
        data = requests.get(url).text
        data = json.loads(data)

    return data['topartist']['artist'][0]['name']
       
    
#     
# 
# import pandas
# baseball_data = pandas.read_csv('Master.csv')
# print baseball_data['nameFirst']
# baseball_data['height_plus_weight'] = baseball_data['height'] + baseball_data['weight']
# baseball_data.to_csv('baseball_data_with_weight_hight.csv')
# #we create a new file 'baseball_data_with_weight_hight.csv'
# 
# 
# 
# #this code is just an example of SQL, it won't work here.
# import pandas
# import pandasql
# 
# def select_first_50(filename):
#     # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
#     # by replacing spaces with underscores and setting all characters to lowercase, so the
#     # column names more closely resemble columns names one might find in a table.
#     aadhaar_data = pandas.read_csv(filename)
#     aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
# 
#     # Select out the first 50 values for "registrar" and "enrolment_agency"
#     # in the aadhaar_data table using SQL syntax. 
#     #
#     # Note that "enrolment_agency" is spelled with one l. Also, the order
#     # of the select does matter. Make sure you select registrar then enrolment agency
#     # in your query.
#     q = """
#     SELECT
#     registrar, enrolment_agency
#     FROM
#     aadhaar_data
#     LIMIT 50;
#     """
#     #Execute your SQL command against the pandas frame
#     aadhaar_solution = pandasql.sqldf(q.lower(), locals())
#     return aadhaar_solution    
# 
# 
# import pandas
# import pandasql
# 
# def aggregate_query(filename):
#     # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
#     # by replacing spaces with underscores and setting all characters to lowercase, so the
#     # column names more closely resemble columns names one might find in a table.
#     
#     aadhaar_data = pandas.read_csv(filename)
#     aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
# 
#     # Write a query that will select from the aadhaar_data table how many men and how 
#     # many women over the age of 50 have had aadhaar generated for them in each district
#     #
#     # Note that in this quiz, the SQL query keywords are case sensitive. 
#     # For example, if you want to do a sum make sure you type 'sum' rather than 'SUM'.
#     #
# 
#     # The possible columns to select from aadhaar data are:
#     #     1) registrar
#     #     2) enrolment_agency
#     #     3) state
#     #     4) district
#     #     5) sub_district
#     #     6) pin_code
#     #     7) gender
#     #     8) age
#     #     9) aadhaar_generated
#     #     10) enrolment_rejected
#     #     11) residents_providing_email,
#     #     12) residents_providing_mobile_number
#     #
#     # You can download a copy of the aadhaar data that we are passing 
#     # into this exercise below:
#     # https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv
#         
#     q = """
#     SELECT
#         gender
#         , district
#         , sum(aadhaar_generated)
#     FROM
#         aadhaar_data
#     WHERE 
#         age>50
#     GROUP BY
#         gender, district;
#     """
# 
#     # Execute your SQL command against the pandas frame
#     aadhaar_solution = pandasql.sqldf(q.lower(), locals())
#     return aadhaar_solution  