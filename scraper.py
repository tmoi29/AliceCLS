import lxml.html
from lxml.cssselect import CSSSelector

import requests

def scrape(url,tag):
    r = requests.get(url)

    # build the DOM Tree
    tree = lxml.html.fromstring(r.text)

    # print the parsed DOM Tree
    #print lxml.html.tostring(tree)
    
    # construct a CSS Selector
    sel = CSSSelector(tag)

    # Apply the selector to the DOM tree.
    results = sel(tree)
            
    # get the text out of all the results
    data = []
    for result in results:
        data.append(result.text_content())
    #returns a list of text
    return data

def scrape_file(f,tag):
    # build the DOM Tree
    tree = lxml.html.fromstring(open(f,'r').read())

    # print the parsed DOM Tree
    #print lxml.html.tostring(tree)
    
    # construct a CSS Selector
    sel = CSSSelector(tag)

    # Apply the selector to the DOM tree.
    results = sel(tree)
            
    # get the text out of all the results
    data = []
    for result in results:
        data.append(result.text_content())
    #returns a list of text
    return data

def convert(txt):
    try:
        return lxml.html.fromstring(txt).text
    except:
        return ""
