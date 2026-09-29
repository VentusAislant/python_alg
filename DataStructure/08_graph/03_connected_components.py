from collections import defaultdict, deque


def count_connected_components(edges) -> int:
    """
    使用广度优先算法判断连通分量个数（也可以用深度优先遍历）
    :param edges: 图的边集
    :return: 连通分量数量
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def bfs(start):
        queue = deque()
        visited.add(start)
        queue.append(start)
        while queue:
            vertex = queue.popleft()
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    count = 0
    for vertex in graph:
        if vertex not in visited:
            bfs(vertex)
            count += 1
    return count


if __name__ == '__main__':
    edges = ((0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (6, 7))
    print(count_connected_components(edges))

    edges = ((0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (6, 7), (2, 3))
    print(count_connected_components(edges))

    edges = ((0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (6, 7), (2, 3), (5, 6))
    print(count_connected_components(edges))
