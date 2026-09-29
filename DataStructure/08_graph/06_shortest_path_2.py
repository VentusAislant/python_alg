"""
1. 无权图求最短路径，可以直接使用 BFS 算法实现
2. 单源最短路径，可以使用 Dijkstra算法 实现
3. 全源最短路径，可以使用 Floyd-Warshall算法 实现
"""
from collections import defaultdict
import heapq


def dijkstra_shortest_path(edges, start, end):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 记录父节点的和长度的方式来方便复原最短路径
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    parent = {start: None}

    heap = [(0, start)]
    visited = set()

    while heap:
        cur_dist, u = heapq.heappop(heap)  # 从堆中弹出表明到这个节点的最短路径已经确定
        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u]:
            if v in visited:
                continue
            if cur_dist + weight < dist[v]:
                dist[v] = cur_dist + weight
                heapq.heappush(heap, (dist[v], v))
                parent[v] = u

    if dist[end] == float('inf'):
        return float('inf'), []

    shortest_path = []
    cur_end = end
    while cur_end is not None:
        shortest_path.append(cur_end)
        cur_end = parent[cur_end]
    shortest_path.reverse()

    return dist[end], shortest_path


if __name__ == '__main__':
    edges = [
        ('A', 'B', 2), ('A', 'C', 9),
        ('A', 'B', 3), ('B', 'C', 1),
    ]
    print(dijkstra_shortest_path(edges, 'A', 'C'))

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
        ('D', 'G', 0.1),
        ('E', 'G', 1.5),
        ('F', 'H', 4),
        ('G', 'H', 4)
    ]
    print(dijkstra_shortest_path(edges, 'A', 'H'))
