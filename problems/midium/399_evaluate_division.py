from typing import List
from collections import namedtuple


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i in range(len(values)):
            x, y, v = equations[i][0], equations[i][1], values[i]
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x: 1 / v}

        def dfs(s, t):
            if s not in graph:
                return -1
            if t == s:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)
                    v = dfs(node, t)
                    if v != -1:
                        return graph[s][node] * v
            return -1

        res = []
        for qs, qt in queries:
            visited = set()
            res.append(dfs(qs, qt))
        return res


class NewSolution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        class Item:
            def __init__(self, parent, value):
                self.parent = parent
                self.value = value

        father = dict()

        def find(x):
            if x != father[x].parent:
                t = father[x].parent
                father[x].parent = find(t)
                father[x].value *= father[t].value
                return father[x].parent
            return x

        def union(e1, e2, result):
            f1 = find(e1)
            f2 = find(e2)
            if f1 != f2:
                father[f1].parent = f2
                father[f1].value = father[e2].value * result / father[e1].value

        number = {}
        for i in range(len(values)):
            x, y, v = equations[i][0], equations[i][1], values[i]
            if x not in number:
                number[x] = len(number) + 1
                father[number[x]] = Item(number[x], 1)
            if y not in number:
                number[y] = len(number) + 1
                father[number[y]] = Item(number[y], 1)
            e1, e2 = number[x], number[y]
            union(e1, e2, v)

        ans = []
        for s1, s2 in queries:
            if s1 not in number or s2 not in number:
                ans.append(-1.0)
                continue
            e1, e2 = number[s1], number[s2]
            f1, f2 = find(e1), find(e2)
            if f1 != f2:
                ans.append(-1)
            else:
                v1 = father[e1].value
                v2 = father[e2].value
                ans.append(v1 / v2)
        return ans


if __name__ == '__main__':
    print(NewSolution().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))