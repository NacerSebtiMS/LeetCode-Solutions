# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:17:39 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/happy-number/
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        return isHappyRec(n,[])

            
def isHappyRec(n,L):
    if n == 0:
        return False
    if n == 1:
        return True
    s = 0
    while n != 0:
        s += (n%10) ** 2
        n = n//10
    if s in L:
        return False
    L.append(s)
    return isHappyRec(s,L)