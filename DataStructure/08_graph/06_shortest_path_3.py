"""
1. 无权图求最短路径，可以直接使用 BFS 算法实现
2. 单源最短路径，可以使用 Dijkstra算法 实现
3. 全源最短路径，可以使用 Floyd-Warshall算法 实现
"""

def floyd_shortest_path(edges, start, end):
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])

    # dist[a][b] 表示 从节点 a 到节点 b 的当前已知的最短路径长度
    # next_node[a][b] 表示 当前最短路径中，从a到b的最短路径中，下一步走哪个节点
    """
    A --1--> B --1--> C --1--> D
    dist[A][D]=3, next_node[A][D] = B  # 因为最短路径是 A → B → C → D
    dist[B][D]=2, next_node[B][D] = C
    dist[C][D]=1, next_node[C][D] = D
    dist[D][D]=0, next_node[D][D] = D
    """
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}
    nex_node = {u: {v: None for v in nodes} for u in nodes}

    for u in nodes:
        dist[u][u] = 0
    for u, v, w in edges:
        dist[u][v] = w
        nex_node[u][v] = v
        nex_node[v][u] = u

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]: # 以k作为中转可以更近
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nex_node[i][j] = nex_node[i][k]

    if nex_node[start][end] is None:
        return float('inf'), []

    cur_start = start
    path = [cur_start]

    while cur_start != end:
        cur_start = nex_node[cur_start][end]
        path.append(cur_start)

    return dist[start][end], path


if __name__ == '__main__':
    edges = [
        ('A', 'B', 2), ('A', 'C', 9),
        ('A', 'B', 3), ('B', 'C', 1),
    ]
    print(floyd_shortest_path(edges, 'A', 'C'))

    """
        A
       / \
      B   C
     / \   \
    D   E   F
     \ /   /
      G - H
    """
    edges = [
        ('A', 'B', 1), ('A', 'C', 2),
        ('B', 'D', 1), ('B', 'E', 0.5),
        ('C', 'F', 4),
        ('D', 'G', 0.5),
        ('E', 'G', 1.5),
        ('F', 'H', 4),
        ('G', 'H', 4)
    ]

    print(floyd_shortest_path(edges, 'A', 'H'))
