from datetime import datetime

import Heap
from Graph import Graph
from Heap import Heap, EdgeHeapSort
from Dijkstra import Dijkstra
from Kruskal import Kruskal
import random


def kruskal_heapsort_check(G):
    # Kruskal Heap check
    edge_heap = EdgeHeapSort(G.num_edges)
    for v in G.vertex:
        for edge in v.neighbour_list:
            if edge.from_node < edge.to_node:
                edge_heap.insert(edge.from_node, edge.to_node, edge.weight)

    edge_heap.print_heap()


def dijkstra_heap_check(G):
    # Dijkstra Heap check
    BW = [-1] * N
    heap = Heap(N)
    for v in G.vertex:
        for edge in v.neighbour_list:
            BW[edge.to_node] = edge.weight
    print(BW)
    for i in range(len(BW)):
        heap.insert(i, BW[i])

    heap.print_heap()
    print("New")
    heap.reset_heap(3, 100)
    heap.print_heap()

    print("Extract")
    maxim = heap.extract_max()
    print(maxim)
    heap.print_heap()


def dijkstra_bw_check(G, source, target):
    # Dijkstra
    dijkstra = Dijkstra(G, source, target)
    tsd = datetime.now()
    max_bw1, dad1 = dijkstra.max_bw_without_heap()
    tfd = datetime.now()
    diffd = (tfd - tsd).total_seconds()
    # print(dad1)
    print("-" * 30)
    print("Dijkstra: Time taken to execute Max BW without heap: {} seconds".format(diffd))
    print("Maximum BW: {}\nPath: ".format(max_bw1))
    dijkstra.print_path(dad1, source, target)

    tsd = datetime.now()
    max_bw, dad = dijkstra.max_bw_with_heap()
    tfd = datetime.now()
    diffd = (tfd - tsd).total_seconds()
    print("-" * 30)
    print("Dijkstra: Time taken to execute Max BW with heap: {} seconds".format(diffd))
    # print(dad)
    print("Maximum BW: {}\nPath: ".format(max_bw))
    dijkstra.print_path(dad, source, target)
    print("-" * 30)


def kruskal_bw_check(G, source, target):
    # Kruskal
    kruskal = Kruskal(G, source, target)
    # max_span_tree = kruskal.create_max_spanning_tree()
    # max_span_tree.print_graph()
    tsd = datetime.now()
    max_bw, path = kruskal.max_bw_with_heap_sort()
    tfd = datetime.now()
    diffd = (tfd - tsd).total_seconds()
    print("Kruskal: Time taken to execute Max BW with heapsort: {} seconds".format(diffd))
    print("Maximum BW: {}\nPath: ".format(max_bw))
    kruskal.print_path(path)
    print("-" * 30)
    # print(path)


if __name__ == "__main__":
    N = int(input("Enter number of nodes: "))
    degree = int(input("Enter degree of nodes: "))
    print("Started...")
    g = Graph()
    ts = datetime.now()
    Graph = g.create_graph(N, degree)
    tf = datetime.now()
    diff = (tf - ts).total_seconds()
    # print(G.visited_nodes)
    # G.print_graph()
    # print("Degree of nodes: {}".format(G.get_degree()))
    print("Time taken to generate graph of {} nodes: {} seconds".format(N, diff))
    print("Average degree: {}".format((2 * Graph.num_edges / N)))
    print("Number of edges: {}".format(Graph.num_edges))
    print("Vertex length: {}".format(len(Graph.vertex)))

    # generate the source and target vertices numbers
    # src, tgt = [], []
    # for i in range(5):
    #     s = random.randint(0, N - 1)
    #     src.append(s)
    #     while True:
    #         t = random.randint(0, N - 1)
    #         if s != t:
    #             tgt.append(t)
    #             break

    # randomly generated source and target nodes using the above step
    src = [4908, 614, 3161, 2617, 897]
    tgt = [3776, 4493, 2125, 2571, 4513]
    for i in range(5):
        s, t = src[i], tgt[i]
        print("=" * 30)
        print("Source Node: {}, Target Node: {} of Pair {}".format(s, t, i+1))
        dijkstra_bw_check(Graph, s, t)
        kruskal_bw_check(Graph, s, t)
        print("=" * 30)
    del Graph
