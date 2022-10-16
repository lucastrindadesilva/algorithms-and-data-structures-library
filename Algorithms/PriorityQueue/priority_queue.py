#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Implementação da priority queue com lista ordenada
"""

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
        
class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
        self.len = 0
        
    def push(self, person : Person) -> None: #O(n)
        if self.is_empty() or (not self.is_empty() and self.queue[-1].get_priority() > person.get_priority()):
            self.queue.append(person)
            self.len += 1        
        else:
            for item in range(self.len):
                if self.queue[item].get_priority() < person.get_priority():
                    self.queue.insert(item, person)
                    self.len += 1
                    break
            
    def pop(self) -> None: #O(n)
        if not self.is_empty():
            self.queue.pop(0)
            self.len -= 1
            
    def is_empty(self) -> bool: #O(1)
        return True if self.len == 0 else False
    
    def get_len(self) -> int:
        return self.len

    def __str__(self) -> str:
        result = ''
        for item in self.queue:
            result += '[Name] = {} | Priority = {}\n'.format(item.get_name(), item.get_priority())
        return result
 
 
priority_queue = PriorityQueue()   
assert priority_queue.is_empty() is True, "Should be True"

person = Person('Agostinho', 20)
priority_queue.push(person=person)
assert priority_queue.get_len() == 1, "Should be 1"
assert priority_queue.is_empty() is False, "Should be False"

person = Person('João', 45)
priority_queue.push(person=person)
assert priority_queue.get_len() == 2, "Should be 2"
assert priority_queue.is_empty() is False, "Should be False"

person = Person('Maria', 1)
priority_queue.push(person=person)
assert priority_queue.get_len() == 3, "Should be 3"
assert priority_queue.is_empty() is False, "Should be False"

person = Person('José', 70)
priority_queue.push(person=person)
assert priority_queue.get_len() == 4, "Should be 4"
assert priority_queue.is_empty() is False, "Should be False"

print(priority_queue)      

priority_queue.pop()      
assert priority_queue.get_len() == 3, "Should be 3"
assert priority_queue.is_empty() is False, "Should be False"  

print(priority_queue)     

priority_queue.pop()
priority_queue.pop()
assert priority_queue.get_len() == 1, "Should be 1"
assert priority_queue.is_empty() is False, "Should be False"

print(priority_queue)  