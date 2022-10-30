#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Implementação de árvore binária
"""

class TreeNode:
    """TreeNode class"""
    def __init__(self, value:int|str, left:TreeNode = None, right:TreeNode = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "[Value] = {} | [Left] = {} | [Right] = {}".format(
            self.value, 
            self.left.value if self.left is not None else "",
            self.right.value if self.right is not None else "")

class BinaryTree:
    """Binary Tree Class"""
    
    def __init__(self, value:int|str = None, is_balanced:bool = False) -> None:
        if value is not None:
            self.root = self.create_node(value)
            self.lenght = 1
        else:
            self.root = None
            self.lenght = 0
        self.is_balanced = is_balanced
        
    def create_node(self, value:int|str) -> bool:
        """Creates a new Node"""
        try:
            node = TreeNode(value)
        except:
            return False
        finally:
            return node
            
    def insert(self, value:int|str) -> bool:
        """Creates a new node in the Tree"""
        new_node = self.create_node(value)
        if not new_node:
            return False
        if self.lenght > 0:
            if self.__insert(new_node=new_node):
                self.lenght += 1
                if self.is_balanced:
                    self.__to_balance()
                return True
            else:
                return False
        else:
            self.root = new_node
            return True
        
    def remove(self, value:int|str) -> bool:
        """Remove a value in the Tree, if exists"""
        pass

    def __insert(self, new_node:TreeNode(value), node:TreeNode=self.root, anterior_node:TreeNode=None) -> bool:
        if node.value == value:
            return False #no duplicates
        elif node.value > value:
            if node.left is not None:
                return self.__insert(value=value, node=node.left, anterior_node=node)
            else:
                node.left = new_node
                return True
        else: #node.value < value
            if node.right is not None:
                return self.__insert(value=value, node=node.right, anterior_node=node)
            else:
                node.right = new_node
                return True
    
    
    def __to_balance(self)->None:
        pass

    def get_height(self) -> int: #altura
        """Return the atual height of Tree."""
        pass
    
    def get_width(self) -> int: #largura
        """Return the atual width of Tree."""
        if self.lenght == 0:
            return 0
        width = 1

        node = self.root
        while node.left is not None:
            width += 1
            node = node.left
        
        

    def get_lenght(self)->int:
        return self.lenght

    def search(self, value:int|str, root:TreeNode = self.root) -> bool:
        if root is None:
            return False
        elif root.value == value:
            return True
        elif root.value > value and root.left is not None:
            return self.binary_search(value=value, root=root.left)
        elif root.value < value and root.right is not None:
            return self.binary_search(value=value, root=root.right)
        else:
            return False
    
    def __str__(self) -> str:
        text = "============ Tree ============\n"
        text += "Vertexes: [\n"
        for vertex in self.adjacencies.keys():
            text += str(vertex) + ": | OutDegree = " + str(self.get_outdegree(vertex=vertex))  + " | InDegree = " + str(self.get_indegree(vertex=vertex)) + "\n"
        text += "]\n"
        text += "Edges:\n"
        for vertex in self.adjacencies.keys():
            for edge in self.adjacencies[vertex]:
                text += str(vertex) + " ------(" + str(edge[1]) + ")------> " + str(edge[0]) + "\n"
        return text


string_tree = BinaryTree('A')
print(string_tree)

integer_tree = BinaryTree(1)
print(integer_tree)