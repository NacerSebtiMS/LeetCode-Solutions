# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:29:04 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/zigzag-conversion/
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        R = [""]*numRows
        i=0
        exp = 1
        while(s!=""):            
            if(i==numRows-1 or i==0):
                exp+=1
            R[i] += s[0]
            s = s[1:]
            sign = (-1) ** exp
            i += sign
            
        result = ""
        for string in R:
            result+=string
        return result