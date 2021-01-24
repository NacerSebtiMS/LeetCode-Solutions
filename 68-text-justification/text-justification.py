# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:52:34 2021

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/text-justification/
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        output = []
        line = []
        j = 0
        
        for i in range(len(words)):
            if line == [] :
                line += [words[i]]
            elif lenLine(line) + len(words[i]) + 1 <= maxWidth :
                line += [' ', words[i]]
            else :
                line = addSpace(line,maxWidth)
                output += [fuseLine(line)]
                line = [words[i]]
                
        line += [' ' * (maxWidth - lenLine(line))]
        output += [fuseLine(line)]
        
        return output
            
def lenLine(L):
    s = 0
    for i in range(len(L)):
        s+=len(L[i])
    return s

def addSpace(line, width):
    if len(line) == 1:
        return line + [' ' * (width - lenLine(line))]
    while(lenLine(line)!=width):
        spacesToAdd = width - lenLine(line)
        for i in range(1,len(line),2):
            if spacesToAdd>0:
                line[i] = line[i] + ' '
                spacesToAdd -= 1
    return line

def fuseLine(L):
    s = ""
    for word in L:
        s+=word
    return s