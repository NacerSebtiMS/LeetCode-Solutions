# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 01:08:15 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/divide-two-integers
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        mini = -2**31
        maxi = 2**31 - 1
        
        q = abs(dividend) // abs(divisor)
        
        if dividend * divisor < 0:
            q *= -1
            
        if q < mini:
            return mini
        elif q > maxi:
            return maxi
        
        return q