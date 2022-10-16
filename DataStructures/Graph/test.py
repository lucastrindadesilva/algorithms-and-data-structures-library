#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graph import Graph

graph = Graph()
graph.new_vertex(vertex=1)
graph.new_vertex(vertex=2)
graph.new_edge(vertex=1, edge=(2,5))
graph.new_edge(vertex=2, edge=(1,3))
print(graph)