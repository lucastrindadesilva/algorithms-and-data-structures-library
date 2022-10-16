#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Implementação de grafo
"""

class Graph:
    """Graph Class using list of adjacencies"""
    def __init__(self) -> None:
        self.adjacencies = {}
      
    def new_vertex(self, vertex:int) -> bool:
        """Creates a new Vertex"""
        if vertex not in self.adjacencies.keys():    
            self.adjacencies[vertex] = []
            return True
        return False
            
    def new_edge(self, vertex:int, edge:tuple) -> bool:
        """Creates a new edge if the vertexes exist in the graph"""
        if (    vertex in self.adjacencies.keys() 
                and edge[0] in self.adjacencies.keys() 
                and edge[0] not in self.adjacencies[vertex]
            ):    
            self.adjacencies[vertex].append(edge)
            return True
        return False
    
    def get_outdegree(self, vertex:int) -> int:#O(1)
        """Outdegree of vertex V is the number of edges which are going out from the vertex V."""
        if vertex in self.adjacencies.keys():
            return len(self.adjacencies[vertex])
        return -1
    
    def get_indegree(self, vertex:int) -> int:#O(v*e)
        """Indegree of vertex V is the number of inward directed graph edges from a given graph vertex in a directed graph."""
        indegree = 0
        for adjacency in self.adjacencies.values():
            for edge_weight in adjacency:
                if vertex == edge_weight[0]:
                    indegree += 1
        return indegree
    
    def __str__(self) -> str:
        text = "============ Graph ============\n"
        text += "Vertexes: [\n"
        for vertex in self.adjacencies.keys():
            text += str(vertex) + ": | OutDegree = " + str(self.get_outdegree(vertex=vertex))  + " | InDegree = " + str(self.get_indegree(vertex=vertex)) + "\n"
        text += "]\n"
        text += "Edges:\n"
        for vertex in self.adjacencies.keys():
            for edge in self.adjacencies[vertex]:
                text += str(vertex) + " ------(" + str(edge[1]) + ")------> " + str(edge[0]) + "\n"
        return text