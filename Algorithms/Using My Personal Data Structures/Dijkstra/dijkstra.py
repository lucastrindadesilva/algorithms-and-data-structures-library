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
        
    def dijkstra(self, root:int|str)->list:
        """Default Dijkstra"""
        
        if root not in self.adjacencies.keys():
            return False
        
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
                    if not visiteds[neighbor]:
                        if distances[neighbor][0] > (node_dist + heighbor_dist):
                            distances[neighbor] = ((node_dist + heighbor_dist), node)  
                        to_visit.insert((distances[neighbor][0], neighbor))
                    
        return distances.items()
    
    
    def dijkstra_target(self, root:int|str, target:int|str)->tuple:
        """Dijkstra to a target node"""
        
        if (root not in self.adjacencies.keys() 
            or target not in self.adjacencies.keys()):
            return False
        
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
                if node == target:
                    break
                for neighbor, heighbor_dist in self.adjacencies[node]:
                    if not visiteds[neighbor]:
                        if distances[neighbor][0] > (node_dist + heighbor_dist):
                            distances[neighbor] = ((node_dist + heighbor_dist), node)  
                        to_visit.insert((distances[neighbor][0], neighbor))
                        
        path = []
        path.append(target)
        node_path = distances[target][1]
        while node_path != root:
            path.append(node_path)
            node_path = distances[node_path][1]
        path.append(root)
        path.reverse()           
        return (distances[target][0], path)
                
