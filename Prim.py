class Graph_prim:
    def __init__(self, num_of_nodes):
        self.v = num_of_nodes
        self.m_graph = [[0 for column in range(num_of_nodes)] for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight):
        self.m_graph[node1][node2] = weight
        self.m_graph[node2][node1] = weight

    def prims_mst(self):
        output = []
        postitive_inf = float('inf')
        selected_nodes = [False for node in range(self.v)]
        result = [[0 for column in range(self.v)] for row in range(self.v)]
        indx = 0
        while(False in selected_nodes):
            minimum = postitive_inf
            start = 0
            end = 0
            for i in range(self.v):
                if selected_nodes[i]:
                    for j in range(self.v):
                        if (not selected_nodes[j] and self.m_graph[i][j]>0):  
                            if self.m_graph[i][j] < minimum:
                                minimum = self.m_graph[i][j]
                                start, end = i, j
            selected_nodes[end] = True
            result[start][end] = minimum
            if minimum == postitive_inf:
                result[start][end] = 0
            indx += 1
            result[end][start] = result[start][end]
        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    output.append([i, j, result[i][j]])    
        return output