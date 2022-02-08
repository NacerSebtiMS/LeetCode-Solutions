# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:00:34 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/add-digits/
"""

class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        s = 0
        for digit in str(num):
            s += int(digit)
        return self.addDigits(s)