#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Implementação da busca binária
"""

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