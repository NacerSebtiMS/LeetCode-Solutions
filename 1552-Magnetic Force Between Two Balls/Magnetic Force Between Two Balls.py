# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 01:39:06 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/magnetic-force-between-two-balls/
"""

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        max_force = (position[-1] - position[0]) // (m-1)
        return search(position,m,0,max_force)
        
def possible(position, m, force):
    last_m_pos = position[0]
    m -= 1
    for pos in position:
        if pos - last_m_pos >= force:
            m -= 1
            last_m_pos = pos
            if m == 0:
                return True
    return False
        
def search(position, m, l, r):
    if l >= r:
        return l
    if l+1 == r:
        if possible(position, m, r):
            return r
        return l
    force = (l+r)//2
    if possible(position, m, force):
        return search(position, m, force, r)
    else:
        return search(position, m, l, force)