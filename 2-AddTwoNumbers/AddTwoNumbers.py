# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 22:08:39 2020

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i=1
        s = l1.val + l2.val
        while(l1.next is not None or l2.next is not None):            
            if(l1.next is not None):
                l1 = l1.next
            else :
                l1.val = 0
            if(l2.next is not None):
                l2 = l2.next
            else :
                l2.val = 0
            s += (l1.val + l2.val) * 10**i
            i += 1
        s = str(s)
        l = ListNode(int(s[0]),None)
        for digit in s[1:]:
            l = ListNode(int(digit),l)
        return l