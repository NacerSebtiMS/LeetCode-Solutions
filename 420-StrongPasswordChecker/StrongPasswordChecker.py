# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 06:16:21 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/strong-password-checker/
"""

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        changes = 0
        n = len(password)
        [repeat,pos] = isNoRepeat(password)
        checks = [isLowerCase(password), isUpperCase(password), isDigitCase(password)]       
        while(repeat):
            if(n>20):
                n-=1
                password = password[:pos] + password[pos+1:]
            elif(n>=6):
                checks = turnCheck(checks)
                password = password[:pos+2] + "&" + password[pos+3:]
            else:
                n+=1
                checks = turnCheck(checks)
                password = password[:pos+2] + "&" + password[pos+2:]
            changes +=1
            [repeat,pos] = isNoRepeat(password)
            
        while(not isChecks(checks)):
            [n,checks] = change(n,checks)
            changes += 1
            
        if(n<6) :
            changes += 6-n
        if(n>20) :
            changes += n-20
        return changes
    
def change(n,checks):
    if(n>20):
        return [n-1,checks]
    elif(n<6):
        return [n+1,turnCheck(checks)]
    else:
        return [n,turnCheck(checks)]
    
def turnCheck(checks):
    for i in range(len(checks)):
        if checks[i] == False:
            checks[i] = True
            return checks
    return checks

def isChecks(checks):
    for check in checks:
        if not check:
            return False
    return True
    
def isStrong(password):
    return len(password)>=6 and len(password)<=20 and isNoRepeat(password) and isLowerCase(password) and isUpperCase(password) and isDigitCase(password)

def isNoRepeat(password):
    pos = None
    cpt=1
    rep = False
    temp = password[0]
    m = 3
    finalPos = pos
    for i in range(1,len(password)):
        if(password[i]==temp):
            cpt+=1
            if(cpt==3):
                pos = i - 2
                rep = True
        if(password[i]!=temp or i==len(password)-1):
            if(cpt%3==0):
                return [rep,pos]
            elif(cpt>3 and cpt%3==1 and m>1):
                m=1
                finalPos = pos
                cpt = 1
            elif(cpt>3 and cpt%3==2 and m>2):
                m=2
                finalPos = pos
                cpt = 1
            else:
                cpt = 1
        temp = password[i]
    if finalPos is None:
        finalPos = pos
    return [rep,finalPos]

def isLowerCase(password):
    for char in password:
        if ord(char)>=ord('a') and ord(char)<=ord('z'):
            return True
    return False

def isUpperCase(password):
    for char in password:
        if ord(char)>=ord('A') and ord(char)<=ord('Z'):
            return True
    return False

def isDigitCase(password):
    for char in password:
        if ord(char)>=ord('0') and ord(char)<=ord('9'):
            return True
    return False
    
    