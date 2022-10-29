#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/evaluate-division/

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""


class Solution:
    def calcEquation(self, equations: list, values: list, queries: list) -> list:
        adjacencies = dict()
        for index in range(len(equations)):
            new_edge = (equations[index][1], values[index])
            if equations[index][0] in adjacencies.keys():
                adjacencies[equations[index][0]].append(new_edge)
            else:
                adjacencies[equations[index][0]] = [new_edge]

            new_edge = (equations[index][0], 1 / values[index])
            if equations[index][1] in adjacencies.keys():
                adjacencies[equations[index][1]].append(new_edge)
            else:
                adjacencies[equations[index][1]] = [new_edge]

        def dfs(root: str, target: str, weight: float = 1, visiteds: set = set(), to_visit: list = list()) -> float:
            if root in adjacencies.keys() and target in adjacencies.keys():
                visiteds.add(root)  # step1 : set as visited
                if root == target:  # step2: stop condition
                    return weight
                for edge in adjacencies[root]:  # step3: read os edges of root
                    if edge[0] not in visiteds:
                        to_visit.append(edge)
                while len(to_visit) > 0:  # step4: for each root edge, call dfs multiping the weights
                    edge = to_visit[0]
                    del (to_visit[0])
                    result = dfs(root=edge[0], target=target, weight=edge[1],
                                 visiteds=visiteds.copy(), to_visit=list())
                    if result != -1.0:  # found in recursion (-1.0 = not found)
                        return weight * result
            return -1.0

        result = []
        for query in queries:
            result.append(
                dfs(root=query[0], target=query[1], weight=1, visiteds=set(), to_visit=list()))
        return result


s = Solution()

equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
assert (s.calcEquation(equations=equations, values=values, queries=queries), [
        6.0, 0.5, -1.0, 1, -1.0], 'Should be [6.0, 0.5, -1.0, 1, -1.0]')


equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
values = [3.0, 4.0, 5.0, 6.0]
queries = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"],
           ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]
assert (s.calcEquation(equations=equations, values=values, queries=queries), [
        360.00000, 0.00833, 20.00000, 1.00000, -1.00000, -1.00000], 'Should be [360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000]')

equations = [["x1", "x2"], ["x2", "x3"], ["x1", "x4"], ["x2", "x5"]]
values = [3.0, 0.5, 3.4, 5.6]
queries = [["x2", "x4"], ["x1", "x5"], ["x1", "x3"], ["x5", "x5"], [
    "x5", "x1"], ["x3", "x4"], ["x4", "x3"], ["x6", "x6"], ["x0", "x0"]]
assert (s.calcEquation(equations=equations, values=values, queries=queries), [
        1.13333, 16.80000, 1.50000, 1.00000, 0.05952, 2.26667, 0.44118, -1.00000, -1.00000], 'Should be [1.13333,16.80000,1.50000,1.00000,0.05952,2.26667,0.44118,-1.00000,-1.00000]')
