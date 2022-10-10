# Library of Algorithms and Data Structures

Hi, I'm Lucas Trindade and this is my Personal Library of Algorithms and Data Structures developed in Python 3.10. Feel free to study here :) .


## Content

The contents of this repository are organized in two folders: Algorithms and Data Structures. Maybe in the future I'll add a folder of implemented design patterns here.

### Algorithms List

- **Add Two Numbers**: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

- **Binary Search**: Binary Search Tree is a node-based binary tree data structure which has the following properties:

	The left subtree of a node contains only nodes with keys lesser than the node’s key.
	The right subtree of a node contains only nodes with keys greater than the node’s key.
	The left and right subtree each must also be a binary search tree..

- **Longest Palindromic Substring**: Given a string s, return the longest palindromic substring in s. A string is called a palindrome string if the reverse of that string is the same as the original string.

- **Palindromic Substrings Counter**: Counter the number of palindromic substrings of a string.

- **Priority Queue**: It is an abstract data-type similar to a regular queue or stack data structure in which each element additionally has a priority associated with it. In a priority queue, an element with high priority is served before an element with low priority. In some implementations, if two elements have the same priority, they are served according to the order in which they were enqueued; in other implementations ordering of elements with the same priority remains undefined.
	> **Note:** While coders often implement priority queues with heaps, they are conceptually distinct from heaps. A priority queue is a concept like a list or a map; just as a list can be implemented with a linked list or with an array, a priority queue can be implemented with a heap or with a variety of other methods such as an unordered array.

- **Two Sum**: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

### Data Structures List

- **Binary Heap**: It is a tree-based data structure, which is a maximally efficient implementation of the priority queue. On a heap, the highest (or lowest) priority element is always stored at the root. , so a heap is a useful data structure when you need to repeatedly remove the object with the highest (or lowest) priority..
	> **Note:** The binary heap was invented by J.W.J. Williams. It is a very useful structure in building priority-queues and is at the heart of the Heapsort algorithm.

### Complexity analysis

I will analyze the worst and best cases for the time complexity of each algorithm or function, using the big-Θ notation to asymptotically limit the growth of the execution time.

#### Algorithms

|Algorithm                |Best Case                          |Worst Case                         |
|----------------|-------------------------------|-----------------------------|
|Add Two Numbers          |Ω(n)            |O(n)            |
|Binary Search          |Ω(1)            |O(logN)            |
|Longest Palindromic Substring          |Ω(1)            |O(n^2)            |
|Palindromic Substrings Counter          |Ω(1)            |O(n^2)            |
|Priority Queue|Ω(n)            |O(n)            |
|Two Sum|Ω(n)            |O(n^2)            |

#### Data Structures

|Data Structure                |Best Case                          |Worst Case                         |
|----------------|-------------------------------|-----------------------------|
|Binary Heap          |Ω(NlogN)            |O(NlogN)            |