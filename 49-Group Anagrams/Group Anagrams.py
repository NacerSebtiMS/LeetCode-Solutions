# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:59:58 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/group-anagrams/
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            arch = convert(s)
            if d.get(arch):
                d[arch].append(s)
            else:
                d[arch] = [s]
        return list(d.values())
    
def convert(s):
    if s == "":
        return ""
    d = {}
    for letter in s:
        if d.get(letter):
            d[letter] += 1
        else:
            d[letter] = 1
    keys = list(d.keys())
    keys.sort()
    output = ""
    for k in keys:
        output += str(d[k]) + str(k)
    return output