from functions import path_finder,data_collecting

#driver code

algorithm = input("Please select your algorithm\n(d = Dijkstra - p = Prim - k = kruskals) => ")

# dijkstra algorithm
if algorithm=="d":
    g = data_collecting("d")
    p1 = int(input("please enter point 1 of the map : "))
    p2 = int(input("please enter point 2 of the map : "))
    D = g.dijkstra(p2)
    print(f"the lowest cost of travel between point {p1} and {p2} using dijkstra algorithm is : {D[p1]}")

# prim's algorithm
elif algorithm=="p":
    g = data_collecting("p")
    p1 = int(input("please enter point 1 of the map : "))
    p2 = int(input("please enter point 2 of the map : "))
    mst = g.prims_mst()
    print(f"the MST of the travel graph based on prim's algorithm is :\n{mst}")
    passenger_path = path_finder(mst,p1,p2,g.v)
    print(f"the most efficence path for the traveler is :\n{passenger_path}")
    cost = 0
    for i in passenger_path:cost += i[2]
    print(f"total cost of travel is {cost}$")

# krusksal's algorithm
elif algorithm=="k":
    g = data_collecting("k")
    p1 = int(input("please enter point 1 of the map : "))
    p2 = int(input("please enter point 2 of the map : "))
    mst = g.kruskals_mst()
    print(f"the MST of the travel graph based on kruskal's algorithm is :\n{mst}")
    passenger_path = path_finder(mst,p1,p2,g.v)
    print(f"the most efficence path for the traveler is :\n{passenger_path}")
    cost = 0
    for i in passenger_path:cost += i[2]
    print(f"total cost of travel is {cost}$")

else:
    print("invalid input !")

