# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:59:51 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        D = {"2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]}
        return comb(D,digits)
        
            
            
def comb(D,digits):
    if digits == "":
        return []
    elif len(digits) == 1:
        return D[digits]
    else :
        return multL(D[digits[0]],comb(D,digits[1:]))
            
def multL(L1,L2):
    result = []
    for e1 in L1:
        for e2 in L2:
            result += [e1+e2]
    return result