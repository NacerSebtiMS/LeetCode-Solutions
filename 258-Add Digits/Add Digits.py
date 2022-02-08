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
        output = 0
        while num != 0:
            digit = num % 10
            num = num // 10
            if output + digit >= 10:
                output = output + digit - 9
            else:
                output += digit
        return output
   

def addDigitsRecursion(num):
    if num <= 9:
        return num
    s = 0
    for digit in str(num):
        s += int(digit)
    return addDigitsRecursion(s)