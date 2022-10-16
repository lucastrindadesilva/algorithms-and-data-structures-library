#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/zigzag-conversion/description/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
 
Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        all_rows = []
        
        if numRows == 0:
            return False
        elif numRows == 1:
            return s
        else:
            rows = {}
            for nr in range(1, numRows+1):
                rows[nr] = []
            
            row = 0
            ascending = True

            for letter in s:
                if row == 0 or numRows == 1:
                    row = 1
                    ascending = True
                elif row == 1:
                    row += 1
                    ascending = True
                elif row == numRows:
                    row -= 1
                    ascending = False
                elif 1 < row < numRows and ascending:
                    row += 1
                elif 1 < row < numRows and not ascending:
                    row -= 1
                
                rows[row].append(letter)
            
            for nr in range(1, numRows+1):
                all_rows += rows[nr]
            
            return ''.join(all_rows)