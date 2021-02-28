
"""
This file contains three functions for extracting features and information from a URL:
@parse_url
@count_digits
@count_symbols
Additional extraction function could be added to this file at a later stage
"""

from urllib.parse import urlparse

#Function for parsing a given URL into smaller strings, necessary for analysis of the URL, 
# as some sub-strings of the URL are modifiable and could therefore possibly be malicous.

def parse_url(url):
    this_protocol = urlparse(url).scheme
    this_domain = (urlparse(url).netloc).split('.')[0]
    this_tld = (urlparse(url).netloc).split('.')[1]
    this_path = urlparse(url).path
    this_params = urlparse(url).params
    this_query = urlparse(url).query
    this_fragment = urlparse(url).fragment

    #Using the "urlparse" library, I create a dictionary containting sub-strings of URL
    parsed_url = {}
    parsed_url['protocol'] = this_protocol
    parsed_url['domain'] = this_domain
    parsed_url['tld'] = this_tld
    parsed_url['path'] = this_path
    parsed_url['params'] = this_params
    parsed_url['query'] = this_query
    parsed_url['fragment'] = this_fragment
    parsed_url['url_length'] = len(url)

    return parsed_url   #returns the dictionary

def count_digits(url):
    digits = sum(i.isdigit() for i in url)  #simple digit counter
    return digits

def count_symbols(url):
    #Counts and saves all symbols separately in dictionary, as they might be needed later on
    symbols = {}     
    symbols['@'] = url.count('@')
    symbols['`'] = url.count('`')
    symbols['%'] = url.count('%')
    symbols['#'] = url.count('#')
    symbols['^'] = url.count('^')   
    symbols['$'] = url.count('$')  
    symbols['&'] = url.count('&')
    symbols['-'] = url.count('-')
    symbols['*'] = url.count('*')
    symbols[':'] = url.count(':')
    symbols['total'] = url.count('`')+url.count('%')+url.count('#')+url.count('^')+url.count('$')+url.count('&')+url.count('-')+url.count('*')+url.count(':')+url.count('@')
    return symbols  #returns dictionary