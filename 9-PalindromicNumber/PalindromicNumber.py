# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:59:25 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/palindrome-number/
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        return x - reverse(x) == 0
        
def reverse(x):
    n = 0
    while(x>0):
        n *= 10
        n += x%10
        x = x//10
    return n