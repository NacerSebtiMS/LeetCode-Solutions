# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 19:50:49 2021

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/trim-a-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root == None :
            return root
        
        if root.val < low :
            root = root.right
            return self.trimBST(root, low, high)
        
        if root.val > high :
            root = root.left
            return self.trimBST(root,low,high)
        
        return TreeNode(root.val, self.trimBST(root.left,low,high), self.trimBST(root.right,low,high))