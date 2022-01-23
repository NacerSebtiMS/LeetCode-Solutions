# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 03:32:26 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/two-sum/
"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        
        if n <= 2:
            return n
        
        lines = {}
        
        for i, point1 in enumerate(points[:-1]):
            for j, point2 in enumerate(points[i+1:]):
                a, b = calc_vector(point1,point2)
                if lines.get((a,b)):
                    if point2 not in lines.get((a,b)):
                        lines[(a,b)].append(point2)                    
                else:
                    lines[(a,b)] = [point1, point2]
            
        return max([ len(line) for line in lines.values()])    
            
            
def calc_vector(p1,p2):
    # y = ax + b such as p1 and p2 are on the line
    if p2[0]-p1[0] == 0 :
        a = p1[0]
        b = None
    else:
        a = (p2[1]-p1[1])/(p2[0]-p1[0])
        b = p1[1] - a * p1[0]
    return a, b