# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:38:20 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/ugly-number-ii/
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        L = [1]
        
        i2 = 0
        i3 = 0
        i5 = 0
        
        while len(L)!=n:
            m = min(2*L[i2], 3*L[i3], 5*L[i5])
            L.append(m)
            if m == 2*L[i2]:
                i2 +=1
            if m == 3*L[i3]:
                i3 +=1
            if m == 5*L[i5]:
                i5 +=1
                
        return L[-1]