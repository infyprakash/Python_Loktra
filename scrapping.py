# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:19:33 2016

@author: prakashchandraprasad
"""


from urllib import urlopen
from bs4 import BeautifulSoup
from urllib2 import HTTPError
def geturlAddress(address):
    try:
        html=urlopen(address)
    except HTTPError:
        return None
    try:
        bsobj=BeautifulSoup(html)
    except AttributeError:
        return None
    return bsobj
url=raw_input("Enter the URL in http:// format")
page=raw_input("Enter the page to be searched")
if not page:
    url=url
else:
    url=url+"/"+page
    
BSobj=geturlAddress(url)
val=raw_input("Enter the keyword to be searched")
namelist=BSobj.findAll(text=val)
if not namelist:
   print "No match found"
else:
   print val+" "+"is found:%d times"%(len(namelist))  

