#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = 0
        n2 = 0
        sum_n = 0
        counter = 0
  
        while l1.val is not None:
            n1 += int(l1.val) * (10 ** int(counter))
            if l1.next is not None:
                l1 = l1.next
            else:
                break
            counter += 1
                
        counter = 0
        while l2.val is not None:
            n2 += int(l2.val) * (10 ** int(counter))
            if l2.next is not None:
                l2 = l2.next
            else:
                break
            counter += 1
                
        sum_n = n1 + n2
        sum_n_str = str(sum_n)
        
        ini_node = ListNode()
        last_node = ListNode()
        for k, v in enumerate(reversed(sum_n_str)):
            l3 = ListNode()
            l3.val = v
            if k > 0:
                last_node.next = l3
            else:
                ini_node = l3
            last_node = l3
        
        return ini_node