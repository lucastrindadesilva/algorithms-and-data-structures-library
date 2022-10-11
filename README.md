# Library of Algorithms and Data Structures

Hi, I'm Lucas Trindade and this is my Personal Library of Algorithms and Data Structures developed in Python 3.10. Feel free to study here :) .

## Content

The contents of this repository are organized in foyr folders: Algorithms, Data Structures, Design Patterns and Problems Solveds.

### Algorithms List

- **Binary Search**: Binary Search Tree is a node-based binary tree data structure which has the following properties:

 The left subtree of a node contains only nodes with keys lesser than the node’s key.
 The right subtree of a node contains only nodes with keys greater than the node’s key.
 The left and right subtree each must also be a binary search tree.

- **Priority Queue**: It is an abstract data-type similar to a regular queue or stack data structure in which each element additionally has a priority associated with it. In a priority queue, an element with high priority is served before an element with low priority. In some implementations, if two elements have the same priority, they are served according to the order in which they were enqueued; in other implementations ordering of elements with the same priority remains undefined.
 
 > **Note:** While coders often implement priority queues with heaps, they are conceptually distinct from heaps. A priority queue is a concept like a list or a map; just as a list can be implemented with a linked list or with an array, a priority queue can be implemented with a heap or with a variety of other methods such as an unordered array.

### Data Structures List

- **Binary Heap**: It is a tree-based data structure, which is a maximally efficient implementation of the priority queue. On a heap, the highest (or lowest) priority element is always stored at the root. , so a heap is a useful data structure when you need to repeatedly remove the object with the highest (or lowest) priority.
 
 > **Note:** The binary heap was invented by J.W.J. Williams. It is a very useful structure in building priority-queues and is at the heart of the Heapsort algorithm.

### Design Patterns List

### Problems Solveds List

- **Add Two Numbers**: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

- **Longest Palindromic Substring**: Given a string s, return the longest palindromic substring in s. A string is called a palindrome string if the reverse of that string is the same as the original string.

- **Palindromic Substrings Counter**: Counter the number of palindromic substrings of a string.

- **Remove Letter To Equalize Frequency**: You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal. Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

- **Two Sum**: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
  
- **Zigzag Conversion**: Write the code that will take a string written in a zigzag pattern and make this conversion given a number of rows.

### Complexity analysis

I will analyze the worst and best cases for the time complexity of each algorithm or function, using the big-Θ notation to asymptotically limit the growth of the execution time.

#### Algorithms

|Algorithm                |Best Case                          |Worst Case                         |
|----------------|-------------------------------|-----------------------------|
|Binary Search          |Ω(1)            |O(logN)            |
|Priority Queue|Ω(n)            |O(n)            |

#### Data Structures

|Data Structure                |Best Case                          |Worst Case                         |
|----------------|-------------------------------|-----------------------------|
|Binary Heap          |Ω(NlogN)            |O(NlogN)            |

#### Design Patterns

|Design Pattern                |Best Case                          |Worst Case                         |
|----------------|-------------------------------|-----------------------------|

#### Problems Solveds

|Problem Solved                |Best Case                          |Worst Case                         |
|----------------|-------------------------------|-----------------------------|
|Add Two Numbers          |Ω(n)            |O(n)            |
|Longest Palindromic Substring          |Ω(1)            |O(n^2)            |
|Palindromic Substrings Counter          |Ω(1)            |O(n^2)            |
|Remove Letter To Equalize Frequency|Ω(1)            |O(n+f) *f = frequency of letters in the given word            |
|Two Sum|Ω(n)            |O(n^2)            |
|Zigzag Conversion|Ω(1)            |O(n)            |
