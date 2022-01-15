# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 14:46:03 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/3sum/
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        D = {
            "positive":[],
            "positive_duplicates":[],
            "zeros":[],
            "negative":[],
            "negative_duplicates":[]
            }
        pos_min = -1
        pos_max = -1
        neg_min = 1
        neg_max = 1
        index_pos = {}
        index_neg = {}
        for i in range(len(nums)):
            if nums[i] > 0:
                if nums[i] in D["positive"]:
                    D["positive_duplicates"].append(nums[i])
                else:
                    D["positive"].append(nums[i])
                    index_pos[nums[i]] = True
                    if pos_min < 0 and pos_max < 0:
                        pos_min, pos_max = nums[i], nums[i]
                    if nums[i] < pos_min:
                        pos_min = nums[i]
                    elif nums[i] > pos_max:
                        pos_max = nums[i]
                        
            elif nums[i] == 0:
                D["zeros"].append(nums[i])
            else:
                if nums[i] in D["negative"]:
                    D["negative_duplicates"].append(nums[i])
                else:
                    D["negative"].append(nums[i])
                    index_neg[nums[i]] = True
                    if neg_min > 0 and neg_max > 0:
                        neg_min, neg_max = nums[i], nums[i]
                    if nums[i] < neg_min:
                        neg_min = nums[i]
                    elif nums[i] > neg_max:
                        neg_max = nums[i]
                        
        D["positive"].sort()
        D["negative"].sort()
                    
        if len(D["zeros"]) >= 3:
            output.append([0,0,0])
            
        zero = False
        if len(D["zeros"]) > 0:
            zero = True
            
        for positive in D["positive"]:
            for negative in D["negative"]:
                L = []
                n = (positive + negative) * -1
                
                if n > 0 :
                    if n <= pos_max and n >= pos_min:
                        if n == positive:
                            if n in D["positive_duplicates"]:
                                L = [negative, positive, positive]
                        else :
                            # if n in D["positive"]:
                            if index_pos.get(n) is not None:
                                if n > positive:
                                    L = [negative, positive, n]
                                else:
                                    L = [negative, n, positive]
                                
                if n < 0:
                    if n <= neg_max and n >= neg_min:
                        if n == negative:
                            if n in D["negative_duplicates"]:
                                L = [negative, negative, positive]
                        else :
                            # if n in D["negative"]:
                            if index_neg.get(n) is not None:
                                if n > negative:
                                    L = [negative, n, positive]
                                else:
                                    L = [n, negative, positive]
                
                if n == 0 and zero:
                    L = [negative, 0, positive]
                
                if L != [] and L not in output:
                    output.append(L)

        
        return output