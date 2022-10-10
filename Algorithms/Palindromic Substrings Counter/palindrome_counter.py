#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Write a function to count the number of palindromic substrings of a string
   ex: 
    'aaa' -> 6
    'abc' -> 3
    'abcba' -> 7
    'aaaa' -> 10
"""

def palindrome_counter(text : str) -> int:
    if len(text) in [0,1]:
        return len(text)
    
    result = len(text)
    for pos in range(len(text)): #small notation = O(n * n/2) | big notation = O(n^2)
        if len(text) > pos + 1:
            result += recursive_palindrome_counter(text=text, idx = pos, idy = pos+1)
        if pos - 1 >= 0 and len(text) > pos + 1:
            result += recursive_palindrome_counter(text=text, idx = pos-1, idy = pos+1)
    return result

def recursive_palindrome_counter(text : str, idx : int, idy : int) -> int:
    if idx >= 0 and len(text) > idy and text[idx] == text[idy]:
        return recursive_palindrome_counter(text=text, idx=idx-1, idy=idy+1) + 1
    return 0

res = palindrome_counter('aaa')
print(res)
res = palindrome_counter('abc')
print(res)
res = palindrome_counter('abcba')
print(res)
res = palindrome_counter('aaaa')
print(res)
    