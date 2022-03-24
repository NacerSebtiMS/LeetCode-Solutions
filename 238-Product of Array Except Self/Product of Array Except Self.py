# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 07:47:50 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/product-of-array-except-self/
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        
        left_slider = 1
        right_slider = 1
        
        for i in range(length):
            k = length - i - 1
            
            answer[i] *= left_slider
            left_slider *= nums[i]
            
            answer[k] *= right_slider
            right_slider *= nums[k]
            
        return answer