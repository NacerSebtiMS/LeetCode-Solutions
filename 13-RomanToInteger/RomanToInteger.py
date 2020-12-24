# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:25:13 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        
        L = {"I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000}
        
        n = 0
        temp = 0
        while(s!=""):
            value = L.get(s[-1])
            if value < temp :
                value = -value
            n += value
            temp = value
            s = s[:-1]
        return n