#Travel assistant (graph algorithms)
this is a project that I built for my friend to help her in her course
<br>
its about finding cheapest path between 2 cities on the map (we simulate cities as nodes and map as the weighted graph) and calculating the lowest cost of travel in the graph (Total weight in the weighted graph between 2 nodes)
<br>
project will be started by running "main.py"
1) graph data entrance is handled by data_collection function in functions.py
2) graph input format is only "node1[space]node2[space]weight" for each edge,
Otherwise, program will face an error, after entering each edge, you can choose
about stopping the edges entrance or continue 
2) Prim's and kruskal's algorithms will first calculate the MST of the 
entered graph, then they will calculate the path and cost between them
with the path_finder function in functions.py
3) Dijkstra's algorithm will only calculate the lowest cost between 2 point of the graph (thats basically how Dijkstra's algorithm works, I will be happy if you write the path as lists like MSTs in Prim's and Kruksal's, this was not in my moood :))
