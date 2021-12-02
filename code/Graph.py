"""
This code generates an undirected graph with weights between 1 and 100.
"""
import random


class Node:
    """
    This class gives information regarding the node of the graph
    """

    def __init__(self):
        self.neighbour_list = []


class Edge:
    """
    This class is concerned with the creation of edges and assigning weights to them
    """

    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    @staticmethod
    def provide_weight():
        """
        return: int
        returns a random integer value between 1 and 100 that will be used as weight of edges in the graph
        """
        return random.randint(1, 10000)


class Graph:
    """
    This class generates an undirected graph as per the degree provided
    """

    def __init__(self):
        self.vertex = []
        self.num_edges = 0
        self.visited_nodes = []

    def create_edge(self, v1, v2, edge_weight):
        self.num_edges += 1
        self.vertex[v1].neighbour_list.append(Edge(v1, v2, edge_weight))
        self.vertex[v2].neighbour_list.append(Edge(v2, v1, edge_weight))

    @staticmethod
    def create_graph(N, node_degree):
        """
        This method generates a graph of N vertices with average node degree as node_degree
        """
        g = Graph()

        # create an empty graph of N nodes
        for i in range(0, N):
            node = Node()
            g.vertex.append(node)
            visit = []
            g.visited_nodes.append(visit)

        for i in range(0, N):
            # create a cyclic graph to make graph as connected
            g.create_edge(i, (i + 1) % N, Edge.provide_weight())
            g.visited_nodes[i].append((i + 1) % N)
            g.visited_nodes[(i + 1) % N].append(i)

        k = node_degree
        if node_degree > 200:
            k += 100

        for i in range(0, N):
            # print("Graph Creation for node {} started".format(i))
            # add other edges as per the minimum degree required from the graph
            d = len(g.visited_nodes[i])
            # print("Node {}, current degree {}".format(i, d))
            while d < node_degree:
                n = random.randint(0, N - 1)
                if n not in g.visited_nodes[i] and n != i:
                    if len(g.visited_nodes[n]) < k:
                        g.visited_nodes[i].append(n)
                        g.visited_nodes[n].append(i)
                        g.create_edge(i, n, Edge.provide_weight())
                        d += 1
            # print("Graph Creation for node {} completed".format(i))
        return g

    def print_graph(self):
        print("Graph print......")
        for i in range(len(self.vertex)):
            print("Node {} -->".format(i), end=" ")
            list_len = len(self.vertex[i].neighbour_list)
            for j in range(list_len):
                v = self.vertex[i].neighbour_list[j]
                print("({}, {}, {}) ".format(v.from_node, v.to_node, v.weight), end=" ")
                if (j + 1) != list_len:
                    print("-> ", end=" ")
            # for v in self.vertex[i].neighbour_list:
            print()

    def get_degree(self):
        for i in range(len(self.vertex)):
            print("Node {} --> degree {}".format(i, len(self.vertex[i].neighbour_list)))

    def get_neighbour(self, v):
        return self.vertex[v].neighbour_list

    def get_bw(self, i, j):
        """
        Returns the bandwidth of the edge between i and j vertices
        """
        for edge in self.vertex[i].neighbour_list:
            if edge.to_node == j:
                return edge.weight
        return -1
