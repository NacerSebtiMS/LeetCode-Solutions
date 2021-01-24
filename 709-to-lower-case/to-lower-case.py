# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:26:32 2021

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/to-lower-case/
"""

class Solution:
    def toLowerCase(self, str: str) -> str:
        uppercase = range(ord('A'),ord('Z')+1)
        for i in range(len(str)):
            if ord(str[i]) in uppercase :
                str = str[:i] + chr(ord(str[i]) - (ord('A')-ord('a'))) + str[i+1:]
        return str