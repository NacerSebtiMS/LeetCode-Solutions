# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:37:45 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j] == target):
                    return [i,j]
        return []