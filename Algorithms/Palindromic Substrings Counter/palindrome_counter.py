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
        if len(text) > pos + 1: #even case
            result += recursive_palindrome_counter(text=text, idx = pos, idy = pos+1)
        if pos - 1 >= 0 and len(text) > pos + 1: #odd case
            result += recursive_palindrome_counter(text=text, idx = pos-1, idy = pos+1)
    return result

def recursive_palindrome_counter(text : str, idx : int, idy : int) -> int:
    if idx >= 0 and len(text) > idy and text[idx] == text[idy]:
        return recursive_palindrome_counter(text=text, idx=idx-1, idy=idy+1) + 1
    return 0

assert palindrome_counter('aaa') == 6, "Should be 6"
assert palindrome_counter('abc') == 3, "Should be 3"
assert palindrome_counter('abcba') == 7, "Should be 7"
assert palindrome_counter('aaaa') == 10, "Should be 10"    