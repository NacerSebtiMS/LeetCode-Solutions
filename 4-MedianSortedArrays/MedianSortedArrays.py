# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:06:58 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

class Solution:
    def findMedianSortedArrays(self, L1: List[int], L2: List[int]) -> float:
        L = []
        while(L1!=[] or L2!=[]):
            if L1 == []:
                L += L2
                L2 = []
            elif L2 == []:
                L += L1
                L1 = []
            else :
                if(L1[0]>L2[0]):
                    L += [L2[0]]
                    L2 = L2[1:]
                else :
                    L += [L1[0]]
                    L1 = L1[1:]
        n = len(L)-1
        if(n%2 == 0):
            return L[n//2]
        else :
            return (L[n//2]+L[n//2+1])/2