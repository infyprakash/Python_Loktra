# -*- coding: utf-8 -*-
"""
Created on Thu May  5 22:55:49 2016

@author: prakashchandraprasad
"""

import random

def hash(str):
   h=7
   letters='acdegilmnoprstuw'
   length=len(str)
   for i in range(length):
      h=h*37 +letters.index(str[i])
   return h
 
def random_gen(len):
   chars='acdegilmnoprstuw'
   return ''.join(random.choice(chars) for x in range(len))

len1=input("enter the length of string to be generated")
alphaString=random_gen(len1)
numericString=hash(alphaString)
print "The generated hash value: ",numericString
