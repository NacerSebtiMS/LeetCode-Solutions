# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 22:21:24 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = []
        max = 0
        for i in range(len(s)):
            if(s[i] not in L):
                L += [s[i]]
            else:
                if(len(L)>max):
                    max = len(L)
                L += [s[i]]
                while(L[0]!=s[i]):
                    L = L[1:]
                L = L[1:]
        if(len(L)>max):
            return len(L)
        return max