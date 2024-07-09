def floyd_warshall(graph):
    n = len(graph)

    dist = [[float('inf')] * n for _ in range (n)]

    for i in range(n):
        dist[i][i]=0
    for u in range(n):
        for v in range(n):
            if graph[u][v] != float('inf'):
                dist[u][v] = graph[u][v]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j])
    
    return dist

if __name__ == "__main__":
     INF = float('inf')
     graph = [
         [0,4,5,INF],
         [1,3,INF,0],
         [2,INF,0,1],
         [INF,3,2,0]
     ]

     shortest_distances = floyd_warshall(graph)
     print("shortest_distances between all pairs of vertices: ")
     for row in shortest_distances:
         print(row)
    