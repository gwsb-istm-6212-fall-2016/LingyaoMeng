#!/usr/bin/env python

import fileinput
import re

def process(line):
    """For each line of input, split the line into words."""      
    eachfind = re.compile('\w+')
    word = eachfind.findall(line)
    
    for i in word:
        if len(i) >=2:
            print (i)        
    
for line in fileinput.input():
    process(line)  