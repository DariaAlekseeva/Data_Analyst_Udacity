from bs4 import BeautifulSoup

def options(soup, id):
    option_values = []
    carrier_list = soup.find(id=id)
    for option in carrier_list.find_all('option'):
        option_values.append(option['value'])
    return option_values

def print_list(label, codes):
    print '\n%s:' % label
    for c in codes:
        print c
        
def main():
    soup = BeautifulSoup(open("virgin_and_airport.html"))
    
    codes = options(soup, "CarrierList")
    print_list("Carriers", codes)
    
    codes = options(soup, 'AirportList')
    print_list("Airports", codes)
    
# main()






#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the approprate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
from bs4 import BeautifulSoup
import requests
import json

html_page = "page_source.html"


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        soup = BeautifulSoup(html)
        ev = soup.find(id="__EVENTVALIDATION")
        data["eventvalidation"] = ev["value"]
        vs = soup.find(id = "__VIEWSTATE")
        data["viewstate"] = vs["value"]     
        
    return data

def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text