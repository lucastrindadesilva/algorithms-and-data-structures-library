#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(os.path.abspath(os.path.join(dir_path, os.pardir)), os.pardir))
sys.path.insert(0, parent_dir_path)

from DataStructures.Graph.graph import Graph
                
class Dfs(Graph):
    """Implementação de busca em profundidade em grafos"""
    def __init__(self) -> None:
        super().__init__()
        
    def dfs(self, root:int, target:int = None, visiteds:list = []) -> list:
        if (root in self.adjacencies.keys()
                and (target is None
                    or (target is not None and target in self.adjacencies.keys())
                    )
            ):
            visiteds.append(root)
            if target is not None and root == target:
                return visiteds
            elif root != target and len(self.adjacencies[root]) > 0:
                for edge in self.adjacencies[root]:
                    if edge[0] not in visiteds:
                        result = self.dfs(root=edge[0],target=target,visiteds=visiteds)
                        if len(result) > 0:
                            return result
                return []
            elif target is None and len(self.adjacencies[root]) == 0:#erro
                return visiteds
            else:
                return []
        else:
            return []
                
            
                         
                
graph = Dfs()
graph.new_vertex(vertex=1)
graph.new_vertex(vertex=2)
graph.new_vertex(vertex=3)
graph.new_vertex(vertex=4)
graph.new_vertex(vertex=5)
graph.new_vertex(vertex=6)
graph.new_vertex(vertex=7)
graph.new_vertex(vertex=8)
graph.new_vertex(vertex=9)
graph.new_vertex(vertex=10)
graph.new_vertex(vertex=11)
graph.new_vertex(vertex=12)
graph.new_edge(vertex=1, edge=(2,0))
graph.new_edge(vertex=1, edge=(3,0))
graph.new_edge(vertex=1, edge=(4,0))
graph.new_edge(vertex=2, edge=(5,0))
graph.new_edge(vertex=2, edge=(6,0))
graph.new_edge(vertex=3, edge=(7,0))
graph.new_edge(vertex=4, edge=(8,0))
graph.new_edge(vertex=4, edge=(9,0))
graph.new_edge(vertex=5, edge=(10,0))
graph.new_edge(vertex=7, edge=(11,0))
graph.new_edge(vertex=9, edge=(12,0))

print(graph)
print(graph.dfs(1,11))