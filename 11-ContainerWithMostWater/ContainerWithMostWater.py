# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 10:45:46 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        m = 0
        while(left<right):
            a = air(height,left,right)
            if(a>m):
                m = a
            if(height[left]<height[right]):
                left += 1
            else :
                right -= 1
        return m
        
def air(L,i,j):
    return abs(i-j) * min(L[i],L[j])

def min(a,b):
    if a<b:
        return a
    return b