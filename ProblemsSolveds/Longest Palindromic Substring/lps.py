#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest palindromic substring in s.
A string is called a palindrome string if the reverse of that string is the same as the original string.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return False
        if len(s) == 1:
            return s

        max = s[0]
        for pos in range(len(s)-1):
            if pos+1 < len(s):
                aux = self.getPalindromeRecursively(s, pos, pos+1)
                if len(aux) > len(max):
                    max = aux
                if pos-1 >= 0:
                    aux = self.getPalindromeRecursively(s, pos-1, pos+1)
                    if len(aux) > len(max):
                        max = aux
        return max



    def getPalindromeRecursively(self, s: str, posA: int, posB: int, max_pal: str = '') -> str:
        if posA >= 0 and posB < len(s) and s[posA] == s[posB]:
            if len(max_pal) < len(s[posA:(posB+1)]):
                max_pal = s[posA:(posB+1)]
            return self.getPalindromeRecursively(s, posA-1, posB+1, max_pal)
        else:
            return max_pal