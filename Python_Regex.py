# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:05:41 2020

@author: sanjay pani
"""

import re

line = "This is sanjay + kumar"

searchObj = re.search("\+", line)

print(searchObj)

if searchObj:
    print("Search Object ", searchObj.group())
else:
    print("No matching found .......")

