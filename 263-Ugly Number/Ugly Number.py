# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:32:39 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/ugly-number/
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        ugly_factors = [2,3,5]
        for factor in ugly_factors:
            while n%factor == 0:
                n = n//factor
        if n == 1:
            return True
        return False