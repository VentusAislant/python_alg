from collections import defaultdict
from collections import deque

# 广度优先遍历
def BFS(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return _BFS(graph, list(graph.keys())[0])

def _BFS(graph, start):
    queue = deque()
    results = []
    visited = set()
    # 访问开始节点
    results.append(start)
    visited.add(start)
    queue.append(start)
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                results.append(neighbor)
                visited.add(neighbor)
                queue.append(neighbor)
    return results


if __name__ == '__main__':
    edges = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (4, 5), (5, 3))
    print(BFS(edges))  # [0, 1, 2, 3, 4, 5]
    edges = ((0, 1), (1, 2), (2, 3), (3, 0))
    print(BFS(edges))  # [0, 1, 3, 2]
    edges = ((0, 1), (1, 2), (2, 3), (3, 4))
    print(BFS(edges))  # [0, 1, 2, 3, 4]
