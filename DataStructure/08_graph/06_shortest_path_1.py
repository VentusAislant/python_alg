"""
1. 无权图求最短路径，可以直接使用 BFS 算法实现
2. 单源最短路径，可以使用 Dijkstra算法 实现
3. 全源最短路径，可以使用 Floyd-Warshall算法 实现
"""
from collections import defaultdict, deque


def bfs_shortest_path(edges, start, end):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 记录父节点的和长度的方式来方便复原最短路径
    distance = {start:0}
    parent = {start:None}

    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                distance[neighbour] = distance[vertex] + 1
                parent[neighbour] = vertex

    # 复原最短路径
    shortest_path = []
    while end is not None:
        shortest_path.append(end)
        end = parent[end]
    shortest_path.reverse()

    return shortest_path, len(shortest_path)-1


if __name__ == '__main__':
    edges  = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (4, 5), (5, 3))
    print(bfs_shortest_path(edges, 0, 5))
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
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'),
        ('D', 'G'),
        ('E', 'G'),
        ('F', 'H'),
        ('G', 'H')
    ]
    print(bfs_shortest_path(edges, 'A', 'G'))

