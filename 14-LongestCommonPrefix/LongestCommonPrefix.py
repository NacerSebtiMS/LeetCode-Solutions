# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:34:18 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/longest-common-prefix/
"""

class Solution:
    def longestCommonPrefix(self, L: List[str]) -> str:
        if L == []:
            return ""
        result = L[0]
        for s in L:
            result = commonPrefix(result,s)
            if result == "":
                return ""
        return result
        
def commonPrefix(s1,s2):
    if s1 == "":
        return ""
    elif s2 == "":
        return ""
    elif s1[0] != s2[0]:
        return ""
    else :
        return s1[0] + commonPrefix(s1[1:],s2[1:])