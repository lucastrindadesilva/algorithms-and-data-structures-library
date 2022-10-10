# Library of Algorithms and Data Structures

Hi, I'm Lucas Trindade and this is my Personal Library of Algorithms and Data Structures developed in Python 3.10. Feel free to study here :) .


## Content

The contents of this repository are organized in two folders: Algorithms and Data Structures

### Algorithms List

- **Palindromic Substrings Counter**: Counter the number of palindromic substrings of a string.

- **Priority Queue**: It is an abstract data-type similar to a regular queue or stack data structure in which each element additionally has a priority associated with it. In a priority queue, an element with high priority is served before an element with low priority. In some implementations, if two elements have the same priority, they are served according to the order in which they were enqueued; in other implementations ordering of elements with the same priority remains undefined.
	> **Note:** While coders often implement priority queues with heaps, they are conceptually distinct from heaps. A priority queue is a concept like a list or a map; just as a list can be implemented with a linked list or with an array, a priority queue can be implemented with a heap or with a variety of other methods such as an unordered array.


### Data Structures List

- **Binary Heap**: It is a tree-based data structure, which is a maximally efficient implementation of the priority queue. On a heap, the highest (or lowest) priority element is always stored at the root. , so a heap is a useful data structure when you need to repeatedly remove the object with the highest (or lowest) priority..
	> **Note:** The binary heap was invented by J.W.J. Williams. It is a very useful structure in building priority-queues and is at the heart of the Heapsort algorithm.

### Complexity analysis

I will only analyze the worst cases for the time complexity of each algorithm or function, using the big-Θ notation to asymptotically limit the growth of the execution time.

|                |Best Case                          |Worst Case                         |
|----------------|-------------------------------|-----------------------------|
|Palindromic Substrings Counter          |Ω(1)            |O(n^2)            |
|Priority Queue|Ω(n)            |O(n)            |
|Binary Heap          |Ω(NlogN)            |O(NlogN)            |