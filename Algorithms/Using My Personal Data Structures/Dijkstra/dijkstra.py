#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Implementação do Algoritmo De Dijkstra
"""

import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(os.path.abspath(os.path.join(dir_path, os.pardir)), os.pardir))
sys.path.insert(0, parent_dir_path)

from DataStructures.Graph.graph import Graph
                
class Dijkstra(Graph):
    """Implementação do Algoritmo De Dijkstra Em Grafos"""
    def __init__(self) -> None:
        super().__init__()
        
    def dijkstra(self, root:int, target:int = None) -> list:
        pass