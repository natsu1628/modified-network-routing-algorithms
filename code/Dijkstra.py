"""
This code implements the Dijkstra's algorithm for maximum bandwidth
"""
from enum import Enum
from Heap import Heap


class Status(Enum):
    FRINGE = 2
    UNSEEN = 0
    IN_TREE = 1


class Dijkstra:
    def __init__(self, graph, source, target):
        self.g = graph
        self.source = source
        self.target = target

    def fringe_with_max_bw(self, status, bw):
        """
        Returns the index of the maximum bandwidth among the fringes
        """
        index_max_bw_fringe = -1
        max_bw_fringe = -1
        for i in range(len(self.g.vertex)):
            if status[i] == Status.FRINGE and bw[i] > max_bw_fringe:
                max_bw_fringe = bw[i]
                index_max_bw_fringe = i
        return index_max_bw_fringe

    def max_bw_without_heap(self):
        dad = [-1] * len(self.g.vertex)
        bw = [-1] * len(self.g.vertex)
        status = [Status.UNSEEN] * len(self.g.vertex)
        status[self.source] = Status.IN_TREE
        fringe_count = 0
        max_bw = -1

        for edge in self.g.vertex[self.source].neighbour_list:
            status[edge.to_node] = Status.FRINGE
            dad[edge.to_node] = edge.from_node
            bw[edge.to_node] = edge.weight
            fringe_count += 1

        while fringe_count > 0:
            v = self.fringe_with_max_bw(status, bw)
            status[v] = Status.IN_TREE
            fringe_count -= 1
            # check if the vertex is the target vertex
            if v == self.target:
                max_bw = bw[self.target]
                break

            for edge in self.g.vertex[v].neighbour_list:
                w = edge.to_node
                # if the vertex is unseen
                if status[w] == Status.UNSEEN:
                    status[w] = Status.FRINGE
                    dad[w] = v
                    fringe_count += 1
                    bw[w] = min(bw[v], edge.weight)
                # if the vertex is a fringe
                elif status[w] == Status.FRINGE and bw[w] < min(bw[v], edge.weight):
                    dad[w] = v
                    bw[w] = min(bw[v], edge.weight)
        return max_bw, dad

    def max_bw_with_heap(self):
        heap = Heap(len(self.g.vertex))

        dad = [-1] * len(self.g.vertex)
        bw = [-1] * len(self.g.vertex)
        status = [Status.UNSEEN] * len(self.g.vertex)
        status[self.source] = Status.IN_TREE
        max_bw = -1
        fringe_count = 0

        for edge in self.g.vertex[self.source].neighbour_list:
            status[edge.to_node] = Status.FRINGE
            dad[edge.to_node] = edge.from_node
            bw[edge.to_node] = edge.weight
            heap.insert(edge.to_node, edge.weight)
            fringe_count += 1

        while fringe_count > 0:
            v, val = heap.extract_max()
            status[v] = Status.IN_TREE
            fringe_count -= 1
            # check if the vertex is the target vertex
            if v == self.target:
                max_bw = bw[self.target]
                break

            for edge in self.g.vertex[v].neighbour_list:
                w = edge.to_node
                # if the vertex is unseen
                if status[w] == Status.UNSEEN:
                    status[w] = Status.FRINGE
                    bw[w] = min(bw[v], edge.weight)
                    dad[w] = v
                    heap.insert(w, bw[w])
                    fringe_count += 1
                # if the vertex is a fringe
                elif status[w] == Status.FRINGE and bw[w] < min(bw[v], edge.weight):
                    bw[w] = min(bw[v], edge.weight)
                    dad[w] = v
                    heap.reset_heap(w, bw[w])
        return max_bw, dad

    @staticmethod
    def print_path(dad, source, target):
        path = []
        v = target
        # print(target, end="->")
        # v = dad[target]
        while v != source:
            # print(v, end="->")
            path.append(v)
            v = dad[v]
        path.append(v)
        # print(v)
        for i in range(len(path) - 1, 0, -1):
            print("{}".format(path[i]), end="->")
        print(path[0])
