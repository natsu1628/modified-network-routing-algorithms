"""
This code implements the heap used in the project
"""


class Heap:
    def __init__(self, N):
        self.max_size = N
        # create array of size N with values as -1
        self.h = [-1] * N
        self.d = [-1] * N
        self.p = [-1] * N
        self.size = 0

    def get_parent(self, pos):
        """
        Returns the position of the parent of the vertex present in the position
        param pos: position of the vertex whose parent needs to be found
        return: position of the parent
        """
        return (pos - 1) // 2

    def get_left_child(self, pos):
        """
        Returns the position of the left child of te vertex present in the position
        param pos: position of the vertex whose left child needs to be found
        return: position of the left child
        """
        return 2 * pos + 1

    def get_right_child(self, pos):
        """
        Returns the position of the right child of te vertex present in the position
        param pos: position of the vertex whose right child needs to be found
        return: position of the right child
        """
        return 2 * pos + 2

    def swap(self, i, j):
        """
        Swaps the position of two vertices in Heap, their corresponding values in the value array, and the positions
        in the position array param i: position of the first vertex param, j: position of the second vertex
        return: None
        """
        self.p[self.h[i]], self.p[self.h[j]] = self.p[self.h[j]], self.p[self.h[i]]
        self.h[i], self.h[j] = self.h[j], self.h[i]

    def max(self):
        """
        Returns the maximum value from the max heap
        """
        return self.h[0]

    def extract_max(self):
        """
        Extracts and returns the maximum element from the heap and then fix the heap
        """
        max_element = (self.h[0], self.d[self.h[0]])
        self.swap(0, self.size - 1)
        self.size = self.size - 1
        self.fix_heap(0)
        return max_element

    def insert(self, vertex, bw):
        """
        This method inserts an element into the max heap
        """
        if self.size > self.max_size:
            print("Error in insert")
        self.h[self.size] = vertex
        self.d[self.h[self.size]] = bw
        self.p[vertex] = self.size
        current = self.size

        while current > 0 and self.d[self.h[current]] > self.d[self.h[self.get_parent(current)]]:
            self.swap(current, self.get_parent(current))
            current = self.get_parent(current)
        self.size += 1

    def fix_heap(self, i):
        left = self.get_left_child(i)
        right = self.get_right_child(i)
        largest = i

        # check if the node is smaller than its left node
        if left != -1:
            if left <= self.size - 1 and self.d[self.h[i]] < self.d[self.h[left]]:
                largest = left
        # check if the node is smaller than its right node
        if right != -1:
            if right <= self.size - 1 and self.d[self.h[largest]] < self.d[self.h[right]]:
                largest = right

        # if largest is not the original node, then swap and fix the heap
        if largest != i:
            self.swap(i, largest)
            self.fix_heap(largest)

    def reset_heap(self, vertex, value):
        """
        This method resets the heap into max heap whenever there is any change in the value inside the heap
        """
        index = self.p[vertex]
        self.d[self.h[index]] = value
        parent = self.get_parent(index)
        while self.d[self.h[parent]] < self.d[self.h[index]]:
            self.swap(parent, index)
            index = parent
            if parent == 0:
                break
            parent = self.get_parent(index)
        self.fix_heap(index)

    def print_heap(self):
        """
        This method prints the whole heap structure with the node and its corresponding values
        """
        for i in range(0, (self.max_size//2)):
            if (2 * i + 2) > self.max_size - 1:
                r = -1
                v = -1
            else:
                r = self.h[2 * i + 2]
                v = self.d[self.h[2 * i + 2]]
            print("P: ({}, {}), L: ({}, {}), R: ({}, {})".format(self.h[i], self.d[self.h[i]], self.h[2 * i + 1], self.d[self.h[2 * i + 1]], r, v))


class EdgeHeapSort:
    def __init__(self, num_edge):
        self.max_size = num_edge
        self.size = 0
        # initialize the target nodes, source nodes and their corresponding weight arrays
        self.s = [-1] * num_edge
        self.t = [-1] * num_edge
        self.d = [-1] * num_edge

    def get_parent(self, pos):
        """
        Returns the position of the parent of the vertex present in the position
        param pos: position of the vertex whose parent needs to be found
        return: position of the parent
        """
        return (pos - 1) // 2

    def get_left_child(self, pos):
        """
        Returns the position of the left child of te vertex present in the position
        param pos: position of the vertex whose left child needs to be found
        return: position of the left child
        """
        return 2 * pos + 1

    def get_right_child(self, pos):
        """
        Returns the position of the right child of te vertex present in the position
        param pos: position of the vertex whose right child needs to be found
        return: position of the right child
        """
        return 2 * pos + 2

    def swap(self, i, j):
        """
        Swaps the position of edges using source nodes, target nodes and their corresponding edge weights
        return: None
        """
        self.t[i], self.t[j] = self.t[j], self.t[i]
        self.s[i], self.s[j] = self.s[j], self.s[i]
        self.d[i], self.d[j] = self.d[j], self.d[i]

    def max(self):
        """
        Returns the maximum value (source, target, capacity) from the max heap
        """
        return self.s[0], self.t[0], self.d[0]

    def extract_max(self):
        """
        Extracts and returns the maximum element from the heap and then fix the heap
        """
        max_element = (self.s[0], self.t[0], self.d[0])
        self.swap(0, self.size - 1)
        self.size = self.size - 1
        self.fix_heap(0)
        return max_element

    def insert(self, source, target, capacity):
        """
        This method inserts an element into the max heap
        """
        if self.size > self.max_size:
            print("Error in insert. Extra elements being added.")

        self.s[self.size] = source
        self.t[self.size] = target
        self.d[self.size] = capacity
        current = self.size

        while current > 0 and self.d[current] > self.d[self.get_parent(current)]:
            self.swap(current, self.get_parent(current))
            current = self.get_parent(current)
        self.size += 1

    def fix_heap(self, i):
        """
        Perform the max heap on the heap to sort the edges in descending order
        """
        left = self.get_left_child(i)
        right = self.get_right_child(i)
        largest = i

        # check if the node is smaller than its left node
        if left != -1:
            if left <= self.size - 1 and self.d[i] < self.d[left]:
                largest = left
        # check if the node is smaller than its right node
        if right != -1:
            if right <= self.size - 1 and self.d[largest] < self.d[right]:
                largest = right

        # if largest is not the original node, then swap and fix the heap
        if largest != i:
            self.swap(i, largest)
            self.fix_heap(largest)

    def print_heap(self):
        """
        This method prints the whole heap structure with the node and its corresponding values
        """
        for i in range(0, (self.max_size//2)):
            if (2 * i + 2) > self.max_size - 1:
                s = -1
                t = -1
                d = -1
            else:
                s = self.s[2 * i + 2]
                t = self.t[2 * i + 2]
                d = self.d[2 * i + 2]
            print("P: ({}, {}, {}), L: ({}, {}, {}), R: ({}, {}, {})".format(self.s[i], self.t[i], self.d[i],
                                                                             self.s[2 * i + 1], self.t[2 * i + 1],
                                                                             self.d[2 * i + 1], s, t, d))
