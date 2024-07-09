import sys

def prims_algorithm(graph):
    V = len(graph)
    selected = [False] * V
    no_edge = 0
    selected[0] = True
    mst_edges = []
    
    print("Edge : Weight")
    while no_edge < V - 1:
        minimum = sys.maxsize
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if (not selected[j]) and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        mst_edges.append((x, y, graph[x][y]))
        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True
        no_edge += 1
    
    return mst_edges

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
]

mst = prims_algorithm(graph)