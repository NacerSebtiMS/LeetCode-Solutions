# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 14:57:23 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/fancy-sequence/
"""

class Fancy:

    def __init__(self):
        self.L = []
        self.M = []
        self.A = []
        self.mod = 10**9 + 7


    def append(self, val):
        self.L.append(val)
        if len(self.M) == 0:
            self.M.append(1)
            self.A.append(0)
        else:
            self.M.append(self.M[-1])
            self.A.append(self.A[-1])
        

    def addAll(self, inc):
        if len(self.A) > 0:
            self.A[-1] = (self.A[-1] + inc) % self.mod
        

    def multAll(self, m):
        if len(self.M) > 0:
            self.M[-1] *= m
            self.A[-1] = (m * self.A[-1]) % self.mod


    def getIndex(self, idx):
        
        n = len(self.L)
        
        if idx >= n:
            return -1
        if idx == 0:
            inc = self.A[-1]
            m = self.M[-1]

        else:
            inc = self.A[-1] - self.A[idx-1] * (self.M[-1]//self.M[idx-1])
            m = self.M[-1]//self.M[idx-1]

        return ( self.L[idx] * m + inc ) % self.mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)