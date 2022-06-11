from Dijkstra import Graph_dijkstra
from Prim import Graph_prim
from kruskals import Graph_kruskals

#calculating distance between 2 point in MST of graph
def path_finder(mst,p1,p2,n):
    try:
        for j in range(n):
            s=0
            for i in mst:
                if i[0]==j or i[1]==j:
                    s+=1
            if s<=1:
                for i in mst[:]:
                    if (i[0]==j or i[1]==j) and j!=p1 and j!=p2:
                        mst.remove(i)
        return path_finder(mst,p1,p2,n)
    except RecursionError:
        return mst
#entrance of datas
def data_collecting(algorithm):
    nodes = int(input("Please enter the number of nodes : "))
    if algorithm=="d": g = Graph_dijkstra(nodes)
    if algorithm=="p": g = Graph_prim(nodes)
    if algorithm=="k": g = Graph_kruskals(nodes)
    action = ""
    while action!="0":
        try:
            node1,node2,weight=map(int,input('please enter the edge ("node1 node2 weight") : ').split())
            g.add_edge(node1,node2,weight)
            action = input("Continue ? (1 = Yes - 0 = Done!) : ")
            while (action!="1" or action!="0"):
                action = input("Please choose between 1 and 0 (1 = Continue of entering edges - 0 = Done with edges !) : ")
        except ValueError:
            print("Enter edge with the correct format! (node1[space]node2[space]weight)")
    return g   