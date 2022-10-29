#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Implementação da priority queue com lista ordenada
"""
import heapq

class Person:
    """
    Classe que será utiizada na lista de prioridades
    Inserção ordenada
    Remove os que tem maior prioridade primeiro
    """
    def __init__(self, name, priority) -> None:
        self.name = name
        self.priority = priority
        
    def get_name(self):
        return self.name
    
    def get_priority(self):
        return self.priority

    def __str__(self)->str:
        return "[Name]: {0} | Priority: {1}".format(self.get_name(),self.get_priority())
 

priority_queue = list()

personA = Person('Agostinho', 20)
priority_queue.append(personA)

personB = Person('João', 45)
priority_queue.append(personB)

personC = Person('Maria', 1)
priority_queue.append(personC)

personD = Person('José', 70)
priority_queue.append(personD)

heap = list()
for pq in priority_queue:
    heap.append((pq.get_priority()*-1,pq)) # *-1for MaxHeap

heapq.heapify(heap)

while len(heap) > 0:
    p, obj = heapq.heappop(heap)
    print(obj)
 