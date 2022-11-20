#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Implementação de árvore binária
"""

class TreeNode:
    """TreeNode class"""
    #def __init__(self, value:tuple, left:TreeNode = None, right:TreeNode = None) -> None:
    def __init__(self, value:tuple, left = None, right = None) -> None:
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
    
    def __init__(self, value:tuple = None, is_balanced:bool = False) -> None:
        if value is not None:
            self.root = self.__create_node(value)
            self.lenght = 1
        else:
            self.root = None
            self.lenght = 0

        self.is_balanced = is_balanced
        
    def __create_node(self, value:tuple) -> bool:
        """Creates a new Node"""
        try:
            node = TreeNode(value)
        except:
            return False
        finally:
            return node
            
    def insert(self, value:tuple) -> bool:
        """Creates a new node in the Tree"""
        new_node = self.__create_node(value)
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
        
    def __insert(self, new_node:TreeNode, node:TreeNode=None, anterior_node:TreeNode=None) -> bool:
        if node is None:
            node = self.root
        if node.value[0] == new_node.value[0]:
            return False #no duplicates
        elif node.value[0] > new_node.value[0]:
            if node.left is not None:
                return self.__insert(new_node=new_node, node=node.left, anterior_node=node)
            else:
                node.left = new_node
                return True
        else: #node.value[0] < new_node.value[0]
            if node.right is not None:
                return self.__insert(new_node=new_node, node=node.right, anterior_node=node)
            else:
                node.right = new_node
                return True
    
    def remove(self, value:tuple) -> bool:
        """Remove a value in the Tree, if exists"""
        pass
    
    def __to_balance(self)->None:
        pass

    def get_height(self) -> int: #altura
        """Return the atual height of Tree."""
        max_height = 0
        
        def get_height_recursive(node:TreeNode, atual_height:int=1):
            nonlocal max_height
            if atual_height > max_height:
                max_height = atual_height
            if node.left is not None:
                get_height_recursive(node.left, atual_height+1)
            if node.right is not None:
                get_height_recursive(node.right, atual_height+1)

        if self.root is not None:
            get_height_recursive(self.root)         
        return max_height
    
    def get_width(self) -> int: #largura
        """Return the atual width of Tree."""
        min_width = 0
        max_width = 0
        
        def get_width_recursive(node:TreeNode, atual_width:int=1):
            nonlocal min_width
            nonlocal max_width
            if atual_width < min_width:
                min_width = atual_width
            if atual_width > max_width:
                max_width = atual_width
            if node.left is not None:
                get_width_recursive(node.left, atual_width-1)
            if node.right is not None:
                get_width_recursive(node.right, atual_width+1)

        if self.root is not None:
            get_width_recursive(self.root)         
        return max_width - min_width
        
    def get_lenght(self)->int:
        return self.lenght

    def search(self, value:tuple, root:TreeNode = None) -> bool:
        root = self.root if root is None else root
        if root.value[0] == value[0]:
            return True
        elif root.value[0] > value[0] and root.left is not None:
            return self.search(value=value, root=root.left)
        elif root.value[0] < value[0] and root.right is not None:
            return self.search(value=value, root=root.right)
        else:
            return False
    
    def __str__(self) -> str:
        if self.lenght == 0:
            return "Empty Tree"
        
        def get_print(node:TreeNode, height:int=0, parent:tuple=None, side:str='center')->dict:
            nodes = {}

            if node is None:
                return
            
            new_node_to_print = {
                side : node.value
            }

            if height not in nodes.keys():
                if parent is None:
                    nodes[height] = {
                        'None' : new_node_to_print
                    }
                else:
                    nodes[height] = {
                        parent : new_node_to_print
                    }
            elif height in nodes.keys() and parent is not None:
                if parent in nodes[height].keys():
                    nodes[height][parent][side] = node.value
                else:
                    nodes[height][parent] = new_node_to_print

            height += 1
            get_print(node=node.left, height=height, parent=node.value, side='left')
            get_print(node=node.right, height=height, parent=node.value, side='right')
        
        nodes = get_print(self.root)
        text = "============ Tree ============\n"
        text += "Width = {}\n".format(self.get_width())
        text += "Height = {}\n".format(self.get_height())
        text += self.__format_str(nodes=nodes)
        return text
    
    def __format_str(self, nodes:dict)->str:  
        result = ""
        
        def run_tree(level:int, parent:int|str)->str:
            #nonlocal result
            text = ""
            if level in nodes.keys() and parent in nodes[level].keys():
                if 'left' in nodes[level][parent].keys():
                    left_node = nodes[level][parent]['left']
                    text += '\n{}|_left: {}'.format((' '*(level-1)), str(left_node))
                    text += run_tree(level=(level+1), parent=left_node)
                if 'right' in nodes[level][parent].keys():
                    right_node = nodes[level][parent]['right']
                    text += '\n{}|_right: {}'.format((' '*(level-1)), str(right_node))
                    text += run_tree(level=(level+1), parent=right_node)
                return text
            else:
                return ""
                
        root = nodes[0]['None']['center']
        result = str(root)
        result += run_tree(level=1,parent=root)
        return result