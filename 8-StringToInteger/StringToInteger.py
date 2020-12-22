# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:53:43 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/string-to-integer-atoi/
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "" :
            return 0
        
        while(s[0] == " "):
            s = s[1:]
            if(s==""):
                return 0
            
        sign = 1
        if s[0] == "+":
            sign = 1
            s = s[1:]
        elif s[0] == "-":
            sign = -1
            s = s[1:]
        
        digits = [chr(i) for i in range(ord("0"),ord("9")+1)]
        
        if s!="" and s[0] in digits:
            n = 0
            while(s!="" and s[0] in digits):
                n *= 10
                n += ord(s[0]) - ord("0")
                s = s[1:]
            n = sign * n
            if(n<(-2)**31):
                return (-2)**31
            elif n > (2**31)-1 :
                return (2**31)-1
            return n
        else :
            return 0