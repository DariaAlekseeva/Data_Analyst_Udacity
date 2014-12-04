import xlrd
from sympy.printing.pretty.pretty import pretty_print
from conda.cli.main_info import pretty_package

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    data = [[sheet.cell_value(r,col)
                for col in range(sheet.ncols)]
                    for r in range(sheet.nrows)]
    
    print "\nList Comprehension"
    print "data[3][2]:",
    print data[3][2]
    
    print "\nCells in a nested loop:"
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50:
                print sheet.cell_value(row, col),
                
    ## other useful methods:
    print "\nROWS, COLUMNS and CELLS:"
    print "Number of rows in the sheet:",
    print sheet.nrows
    print "Type of data in cell (row 3, col 2):",
    print sheet.cell_type(3, 2)
    print "Value in cell (row 3, col 2):",
    print sheet.cell_value(3,2)
    print "Get a slice of values in column 3, from rows 1-3:"
    print sheet.col_values(3, start_rowx=1, end_rowx=4)
    
    print "\nDATES:"
    print "Type of data in cell (row 1, col 0):",
    print sheet.cell_type(1,0)
    exceltime = sheet.cell_value(1,0)
    print "Time in Excel format:",
    print exceltime
    print "Convert time to a Python datatime tuple, from Excel float:",
    print xlrd.xldate_as_tuple(exceltime, 0)
    

# parse_file(datafile)





"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
import numpy
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ## get the data from sheet
    data = [[sheet.cell_value(r, col) 
                      for col in range(sheet.ncols)] 
                          for r in range(sheet.nrows)]
    
    print data
    cv = sheet.col_values(1, start_rowx=1, end_rowx=None)    
    
    maxval = max(cv)
    minval = min(cv)
    
    ## add +1 because our data (cv) was formed from 1 row, not from 0 row.
    maxpos = cv.index(maxval) + 1
    minpos = cv.index(minval) + 1
    
    ## get max and min time according to position of maxval and minval
    maxtime = sheet.cell_value(maxpos, 0)
    realmaxtime = xlrd.xldate_as_tuple(maxtime,0)
    mintime = sheet.cell_value(minpos, 0)
    realmintime = xlrd.xldate_as_tuple(mintime, 0)
    
    data = {
            'maxtime': realmaxtime,
            'maxvalue': maxval,
            'mintime': realmintime,
            'minvalue': minval,
            'avgcoast': numpy.mean(cv)
    }
    print data

parse_file(datafile)










# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    data = "Station|Year|Month|Day|Hour|Max Load\n"                                                  
    nRow = sheet.nrows
    nCol = sheet.ncols

                                                                                                     
    for col in range(1, nCol - 1):                                                                   
        region = sheet.col_values(col)[0]                                                            
        colValues = sheet.col_values(col)[1:]                                                        
        maxLoad = max(colValues)                                                                     
        maxLoadIndex = colValues.index(maxLoad)                                                      
        time = sheet.cell_value(maxLoadIndex, 0)                                                     
        year, month, day, hour, minute, second = xlrd.xldate_as_tuple(time, 0)                       
        hour += 1                                                                                    
        nextline = "|".join( (region, str(year), str(month), str(day), str(hour), str(maxLoad)) )    
        data += nextline + "\n"                                                                      
                                                                                                     
    return data

def save_file(data, filename):
    with open(filename, 'w') as f:                                                                        
        f.write(data)                                                                                    
        f.close()
