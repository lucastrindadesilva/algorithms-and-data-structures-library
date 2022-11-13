#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Implementação da busca binária
"""
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(os.path.abspath(os.path.join(dir_path, os.pardir)), os.pardir))
sys.path.insert(0, parent_dir_path)

from DataStructures.BinaryTree.binary_tree import BinaryTree

def bst(root, target) -> bool:
   """Binary Search Tree"""
   if root is None:
       return False
   elif root.value == target:
       return True
   elif root.value > target and root.left is not None:
       return bst(root.left, target)
   elif root.value < target and root.right is not None:
       return bst(root.right, target)
   else:
       return False
   
 
 
### tests:  
integer_tree = BinaryTree(3)

integer_tree.insert(2)
integer_tree.insert(5)

print(bst(integer_tree.root, 10))
print(integer_tree)

integer_tree.insert(1)
integer_tree.insert(3)
integer_tree.insert(3)
integer_tree.insert(4)
integer_tree.insert(5)
integer_tree.insert(10)
integer_tree.insert(6)

print(bst(integer_tree.root, 10))
print(integer_tree)