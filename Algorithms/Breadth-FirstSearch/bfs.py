#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(os.path.abspath(os.path.join(dir_path, os.pardir)), os.pardir))
sys.path.insert(0, parent_dir_path)

from DataStructures.Graph.graph import Graph
                
class Bfs(Graph):
    """Implementação de busca em largura em grafos"""
    def __init__(self) -> None:
        super().__init__()
        
    def bfs(self, root:int, target:int = None) -> list:
        visiteds = []
        to_visit = []
        
        while True:
            
            if (root in self.adjacencies.keys()
                and (target is None
                    or (target is not None and target in self.adjacencies.keys())
                    )
            ):
                visiteds.append(root)
                if target is not None and root == target:
                    return visiteds
                
                for edge in self.adjacencies[root]:
                    if edge[0] not in visiteds:
                        to_visit.append(edge[0])
        
                if len(to_visit) > 0:
                    root = to_visit[0]
                    del(to_visit[0])
                else:
                    return visiteds
            else:
                return []
                
            
                         
                
graph = Bfs()
graph.new_vertex(vertex=1)
graph.new_vertex(vertex=2)
graph.new_edge(vertex=1, edge=(2,5))
graph.new_edge(vertex=2, edge=(1,3))
graph.new_vertex(vertex=3)
graph.new_edge(vertex=3, edge=(1,10))
graph.new_edge(vertex=3, edge=(2,60))
graph.new_edge(vertex=2, edge=(3,160))
print(graph)
print(graph.bfs(1,2))
print(graph.bfs(1,3))