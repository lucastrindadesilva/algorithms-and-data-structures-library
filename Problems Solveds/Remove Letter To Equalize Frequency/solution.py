#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/

You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.
Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:
The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot chose to do nothing.
 
Example 1:
Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.

Example 2:
Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
 
Constraints:
2 <= word.length <= 100
word consists of lowercase English letters only.
"""
class Solution:
    def equalFrequency(self, word: str) -> bool:
        '''
        word = '' -> false
        len(word) in [1,2] -> true

        '''
        if len(word) == 0:
            return False
        if len(word) in [1,2]:
            return True

        counter = {} #dicionario principal
        letters = {} #parece especial, mas é apenas auxiliar

        #inicializa o dicionario counter
        for index in range(1, len(word)+1):
            counter[index] = []

        #popula o dicionario counter
        for letter in word:
            if letter in letters.keys():
                counter[letters[letter]].remove(letter)
                letters[letter] += 1
                counter[letters[letter]].append(letter)
            else:
                letters[letter] = 1
                counter[1].append(letter)

        for key, value in counter.items():
            if len(value) == len(letters) and key == 1:
                return True
            elif len(value) == len(letters) and key != 1:
                return False
            elif ((len(value) == len(letters)-1 and len(counter[key+1]) == 1)
                or (len(value) == len(letters)-1 and len(counter[1]) == 1 and key != 1)
            ):
                return True
        return False