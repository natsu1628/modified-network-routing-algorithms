"""
This code implements the Kruskal Algorithm for maximum bandwidth
"""
from Heap import EdgeHeapSort
from queue import Queue
from enum import Enum
import Graph
import sys


class Color(Enum):
    GRAY = 2
    BLACK = 1
    WHITE = 0


class Kruskal:
    def __init__(self, graph, source, target):
        self.g = graph
        self.source = source
        self.target = target

    def edge_heap_sort(self):
        edge_heap = EdgeHeapSort(self.g.num_edges)
        for v in self.g.vertex:
            for edge in v.neighbour_list:
                if edge.from_node < edge.to_node:
                    edge_heap.insert(edge.from_node, edge.to_node, edge.weight)
        return edge_heap

    @staticmethod
    def find(v, parent):
        w = v
        s = Queue()
        while parent[w] != -1:
            s.put(w)
            w = parent[w]
        while not s.empty():
            parent[s.get()] = w
        return w

    @staticmethod
    def union(rank1, rank2, rank, parent):
        if rank[rank1] > rank[rank2]:
            parent[rank2] = rank1
        elif rank[rank1] < rank[rank2]:
            parent[rank1] = rank2
        else:
            parent[rank1] = rank2
            rank[rank2] += 1

    def _dfs(self, max_spanning_tree, color, parent, source, target):
        """
        This method uses DFS to assign parent to the maximum spanning tree
        """
        if source == target:
            return True
        color[source] = Color.GRAY
        is_target = False
        for edge in max_spanning_tree.vertex[source].neighbour_list:
            if color[edge.to_node] == Color.WHITE:
                parent[edge.to_node] = edge.from_node
                is_target = self._dfs(max_spanning_tree, color, parent, edge.to_node, target)
                if is_target:
                    break
        color[source] = Color.BLACK
        return is_target

    def create_max_spanning_tree(self):
        N = len(self.g.vertex)
        edge_sort = self.edge_heap_sort()
        max_spanning_tree = Graph.Graph()
        for i in range(N):
            max_spanning_tree.vertex.append(Graph.Node())

        parent = [-1] * N
        rank = [-1] * N
        while edge_sort.size >= 0:
            s, t, d = edge_sort.extract_max()
            r1 = self.find(s, parent)
            r2 = self.find(t, parent)
            if r1 != r2:
                max_spanning_tree.create_edge(s, t, d)
                self.union(r1, r2, rank, parent)
        return max_spanning_tree

    def max_bw_with_heap_sort(self):
        max_spanning_tree = self.create_max_spanning_tree()
        N = len(self.g.vertex)
        parent = [-1] * N
        color = [Color.WHITE] * N

        # apply dfs to get the parents of each vertex in the maximum spanning tree
        self._dfs(max_spanning_tree, color, parent, self.source, self.target)

        max_bw = sys.maxsize
        path = []
        t = self.target
        while t != self.source:
            path.append(t)
            max_bw = min(max_bw, max_spanning_tree.get_bw(t, parent[t]))
            t = parent[t]
        path.append(t)
        return max_bw, path

    @staticmethod
    def print_path(path):
        for i in range(len(path) - 1, 0, -1):
            print("{}".format(path[i]), end="->")
        print(path[0])
