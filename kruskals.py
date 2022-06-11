class Graph_kruskals:
    def __init__(self, num_of_nodes):
        self.v = num_of_nodes
        self.m_graph = []

    def add_edge(self, node1, node2, weight):
        self.m_graph.append([node1, node2, weight])
    
    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_subtree(parent, parent[i])

    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1

    def kruskals_mst(self):
        result = []
        i = 0
        e = 0
        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])
        parent = []
        subtree_sizes = []
        for node in range(self.v):
            parent.append(node)
            subtree_sizes.append(0)
        while e < (self.v - 1):
            node1, node2, weight = self.m_graph[i]
            i = i + 1
            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)
            if x != y:
                e = e + 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)
        return result