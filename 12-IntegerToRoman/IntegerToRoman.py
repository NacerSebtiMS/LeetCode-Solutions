# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:09:37 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/integer-to-roman/
"""

class Solution:
    def intToRoman(self, n: int) -> str:
        
        result = writeDigit( ["I","V","X"], n%10 )
        n = n // 10
        
        result = writeDigit( ["X","L","C"], n%10 ) + result
        n = n // 10
        
        result = writeDigit( ["C","D","M"], n%10 ) + result
        n = n // 10
        
        result = writeDigit( ["M","",""], n%10 ) + result
        
        return result
        
def writeDigit(symbols,digit):
    if digit<=3 :
        return symbols[0] * digit
    elif digit == 4 :
        return symbols[0] + symbols[1]
    elif digit == 5 :
        return symbols[1]
    elif digit <= 8 :
        return symbols[1] + (symbols[0] * (digit-5))
    elif digit == 9 :
        return symbols[0] + symbols[2]