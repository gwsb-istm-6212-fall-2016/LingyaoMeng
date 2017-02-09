#!/usr/bin/env python

"""
A filter that changes all words to lowercase.
"""

import fileinput

def lowercase(word):
    """For each word of input, change the word to all lower case."""
    print (word.lower())  

for line in fileinput.input():
    lowercase(line)