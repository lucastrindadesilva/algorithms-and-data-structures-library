#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from pathlib import Path
main_path = str(Path(__file__).parents[3])
sys.path.insert(0, main_path)

from DataStructures.Graph.graph import Graph
                
class AStar(Graph):
    """Implementação de busca a-estrela em grafos"""
    def __init__(self) -> None:
        super().__init__()
        
        
    def a_star(self, root:int, target:int = None) -> list:
        pass