# Python code to count the number of indexed pages a website has to help you monitor its size and growth rate

import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def get_results(url):
    
    # query = urllib.parse.quote_plus(url)
    # print(query)
    response = get_source("https://www.google.ca/search?q=site%3A" + url)
    # response = get_source(url)
    return response

def parse_results(response):
    string = response.html.find("#result-stats", first=True).text
    # string = response.html.find("#contents", first=True).text
    indexed = int(string.split(' ')[1].replace(',',''))
    return indexed

def count_indexed_pages(url):
    response = get_results(url)
    return parse_results(response)

x = count_indexed_pages("http://flyandlure.org")
# string =  x.html.find("#content", first=True).text
print(int(x.split(' ')[1]))
# print(x)
