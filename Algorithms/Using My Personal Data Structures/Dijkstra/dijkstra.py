#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Implementação do Algoritmo De Dijkstra
"""

import sys
from pathlib import Path
main_path = str(Path(__file__).parents[3])
sys.path.insert(0, main_path)

from DataStructures.Graph.graph import Graph
from DataStructures.BinaryHeap.heap import MinHeap
                
class Dijkstra(Graph):
    """Implementação do Algoritmo De Dijkstra Em Grafos"""
    def __init__(self) -> None:
        super().__init__()
        
    def dijkstra(self, root:int|str, target:int|str = None) -> int|list:
        visiteds = {}
        to_visit = MinHeap()
        distances = {}
        
        for adj in self.adjacencies.keys():
            visiteds[adj] = False
            if adj == root: 
                distances[adj] = (0, adj)
            else: 
                distances[adj] = (float('inf'), None)
                
        to_visit.insert(distances[root])
        
        while to_visit.lenght > 0:
            node_dist, node = to_visit.remove()
            if not visiteds[node]:
                visiteds[node] = True
                for neighbor, heighbor_dist in self.adjacencies[node]:
                    if distances[neighbor][0] > (node_dist + heighbor_dist):
                        distances[neighbor] = ((node_dist + heighbor_dist), node)  
                    to_visit.insert(distances[neighbor])
                    
        return distances[target] if target is not None else distances.items()
                
graph = Dijkstra()
graph.new_vertex("a")
graph.new_vertex("b")
graph.new_vertex("c")
graph.new_vertex("d")
graph.new_vertex("e")
graph.new_vertex("f")
graph.new_vertex("g")
graph.new_vertex("h")
graph.new_edge("a", ("b", 8))
graph.new_edge("a", ("c", 3))
graph.new_edge("a", ("d", 6))
graph.new_edge("b", ("a", 8))
graph.new_edge("b", ("e", 5))
graph.new_edge("c", ("a", 3))
graph.new_edge("c", ("d", 2))
graph.new_edge("d", ("a", 6))
graph.new_edge("d", ("c", 2))
graph.new_edge("d", ("e", 5))
graph.new_edge("d", ("g", 3))
graph.new_edge("e", ("b", 5))
graph.new_edge("e", ("d", 5))
graph.new_edge("e", ("f", 5))
graph.new_edge("f", ("e", 5))
graph.new_edge("f", ("g", 3))
graph.new_edge("f", ("h", 6))
graph.new_edge("g", ("d", 3))
graph.new_edge("g", ("f", 3))
graph.new_edge("g", ("h", 4))
graph.new_edge("h", ("g", 4))
graph.new_edge("h", ("f", 6))
print(graph)   

distances = graph.dijkstra(root="a")
print(distances)
#{'a': 0, 'c': 3, 'd': 5, 'b': 8, 'g': 8, 'e': 10, 'f': 11, 'h': 12}