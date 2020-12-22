# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:37:08 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
            x = -1 * revPositive(-x)
        else:
            x = revPositive(x)
        if(x<(-2)**31 or x>(2**31)-1):
            return 0
        return x
        
def revPositive(x):
    n = 0
    while(x>0):
        n *= 10
        n += x%10
        x = x//10
    return n