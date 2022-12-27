#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Implementação da heap binária
"""

class Heap:
   """Binary Heap Class"""
   def __init__(self)->None:
      self.heap = []
      self.lenght = 0
   
   def get_left(self, position:int)->tuple:
      left = (2*position) + 1
      if 0 <= left < self.lenght:
         return left
      return False
   
   def get_right(self, position:int)->tuple:
      right = (2*position) + 2
      if 0 < right < self.lenght:
         return right
      return False
   
   def get_father(self, position:int)->tuple:
      if 0 < position < self.lenght:
         if position % 2 == 0: #even
            return (position // 2) - 1
         else:#odd
            return position // 2
      else:
         return False
               
   def __str__(self)->str:
      str_heap = [str(h) for h in self.heap] 
      return '|'.join(str_heap)
   
class MinHeap(Heap):
   """Binary Minimum Heap Class"""
   def __init__(self)->None:
      super().__init__()
      
   def insert(self, value:tuple)->None: #O(NlogN)
      ### insere o novo valor no final do heap
      self.heap.append(value)
      self.lenght += 1
      ### reordena o heap para que o novo elemento do final assuma sua nova posição
      if self.lenght > 1:
         position = self.lenght - 1
         while(self.get_father(position) is not False
               and self.heap[self.get_father(position)][0] > self.heap[position][0]):
            swap = self.heap[self.get_father(position)]
            self.heap[self.get_father(position)] = self.heap[position]
            self.heap[position] = swap
            position = self.get_father(position)
            
   def remove(self)->tuple:
      ### remove o elemento que está no topo - armazena o valor para retornar
      result = self.heap[0]
      ### o último elemento se torna o primeiro
      self.heap[0] = self.heap[-1]
      del(self.heap[-1])
      self.lenght -= 1
      ### reordena o heap para que o novo elemento do topo assuma sua nova posição
      position = 0
      while True:
         if self.get_left(position) is not False and self.heap[self.get_left(position)][0] < self.heap[position][0]:
            swap = self.heap[position]
            self.heap[position] = self.heap[self.get_left(position)]
            self.heap[self.get_left(position)] = swap
            position = self.get_left(position)
         elif self.get_right(position) is not False and self.heap[self.get_right(position)][0] < self.heap[position][0]:
            swap = self.heap[position]
            self.heap[position] = self.heap[self.get_right(position)]
            self.heap[self.get_right(position)] = swap
            position = self.get_right(position)
         else:
            break
      ### retorna o valor que estava no topo
      return result    
   
class MaxHeap(Heap):
   """Binary Maximum Heap Class"""
   def __init__(self)->None:
      super().__init__()
      
   def insert(self, value:tuple)->None: #O(NlogN)
      ### insere o novo valor no final do heap
      self.heap.append(value)
      self.lenght += 1
      ### reordena o heap para que o novo elemento do final assuma sua nova posição
      if self.lenght > 1:
         position = self.lenght - 1
         while(self.get_father(position) is not False
               and self.heap[self.get_father(position)][0] < self.heap[position][0]):
            swap = self.heap[self.get_father(position)]
            self.heap[self.get_father(position)] = self.heap[position]
            self.heap[position] = swap
            position = self.get_father(position)
            
   def remove(self)->tuple:
      ### remove o elemento que está no topo - armazena o valor para retornar
      result = self.heap[0]
      ### o último elemento se torna o primeiro
      self.heap[0] = self.heap[-1]
      del(self.heap[-1])
      self.lenght -= 1
      ### reordena o heap para que o novo elemento do topo assuma sua nova posição
      position = 0
      while True:
         if self.get_left(position) is not False and self.heap[self.get_left(position)][0] > self.heap[position][0]:
            swap = self.heap[position]
            self.heap[position] = self.heap[self.get_left(position)]
            self.heap[self.get_left(position)] = swap
            position = self.get_left(position)
         elif self.get_right(position) is not False and self.heap[self.get_right(position)][0] > self.heap[position][0]:
            swap = self.heap[position]
            self.heap[position] = self.heap[self.get_right(position)]
            self.heap[self.get_right(position)] = swap
            position = self.get_right(position)
         else:
            break
      ### retorna o valor que estava no topo
      return result 