# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 23:35:11 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/3sum-closest/
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:     
        n = len(nums)
        
        if n == 3:
            return sum(nums)
        m = None
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    s = nums[i] + nums[j] + nums[k]
                    if s == target:
                        return target
                    if m is None or abs(m-target) > abs(s-target):
                        m = s
        return m