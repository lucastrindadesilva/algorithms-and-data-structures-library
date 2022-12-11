#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(os.path.abspath(os.path.join(dir_path, os.pardir)), os.pardir))
sys.path.insert(0, parent_dir_path)

from DataStructures.Graph.graph import Graph
                
class AStar(Graph):
    """Implementação de busca a-estrela em grafos"""
    def __init__(self) -> None:
        super().__init__()
        
        
    def a_star(self, root:int, target:int = None) -> list:
        pass