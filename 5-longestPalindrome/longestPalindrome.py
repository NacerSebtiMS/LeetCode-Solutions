# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 12:49:41 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/longest-palindromic-substring
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if isPalindrome(s):
            return s 
        
        output = s[0]
        n = len(s)
        
        for i in range(1,n-1):
            j=len(output)//2-1       
            if s[i] == s[i+1]:
                # search for palindrome with i i+1 as center
                while i-j >=0 and i+j+2 <= n and isPalindrome(s[i-j:i+j+2]):
                    if len(output) < len(s[i-j:i+j+2]):
                        output = s[i-j:i+j+2]
                    j+=1
            j=len(output)//2-1 
                
            if s[i] == s[i-1]:
                # search for palindrome with i i-1 as center
                while i-j-1 >=0 and i+j+1 <= n and isPalindrome(s[i-1-j:i+j+1]):
                    if len(output) < len(s[i-1-j:i+j+1]):
                        output = s[i-1-j:i+j+1]
                    j+=1
                    
            j=len(output)//2-1 
                
            if s[i-1] == s[i+1]:
                # search for palindrome with i as center
                while i-j-1 >=0 and i+j+2 <= n and isPalindrome(s[i-j-1:i+j+2]):
                    if len(output) < len(s[i-j-1:i+j+2]):
                        output = s[i-j-1:i+j+2]
                    j+=1
                    
        return output
            
def isPalindrome(s):
    for i in range(len(s)//2):
        if(s[i] != s[-i-1]):
            return False
    return True