from collections import defaultdict

# 深度优先遍历
def DFS(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return _DFS(graph, list(graph.keys())[0], set(), list())

def _DFS(graph, start, visited, results):
    visited.add(start)
    results.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            _DFS(graph, neighbor, visited, results)
    return results

if __name__ == '__main__':
    edges = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (4, 5), (5, 3))
    print(DFS(edges))  # [0, 1, 2, 4, 5, 3]
    edges = ((0, 1), (0, 2), (0, 3), (1, 4), (1, 2), (4, 5), (5, 3))
    print(DFS(edges))  # [0, 1, 4, 5, 3, 2]
    edges = ((0, 1), (1, 2), (2, 3), (3, 0))
    print(DFS(edges))  # [0, 1, 2, 3]
    edges = ((0, 1), (1, 2), (2, 3), (3, 4))
    print(DFS(edges))  # [0, 1, 2, 3, 4]
