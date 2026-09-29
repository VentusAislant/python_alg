"""
拓扑排序：
    1. Kahn算法，基于节点入度的算法，每次取出入度为0的节点加入排序序列
    2. DFS遍历时的递归栈的逆序是拓扑排序
"""

from collections import defaultdict, deque


def kahn_topological_sort(edges):
    nodes = set()
    for u, v in edges:
        nodes.add(u)
        nodes.add(v)
    in_degree = {node: 0 for node in nodes}
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque()
    # 将入度为0的入队
    for node, d in in_degree.items():
        if d == 0:
            queue.append(node)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)  # 需要出队处理

    if len(result) != len(nodes):
        return None  # 存在环

    return result


def dfs_topological_sort(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        # 访问完所有邻居才将当前节点加入栈
        result.append(node)

    for node in list(graph.keys()):
        if node not in visited:
            dfs(node)

    result.reverse()
    return result


if __name__ == '__main__':
    """
      A → C → D → E → F → G → H
      ↘   ↘               ↑
        → B → --------------  
    """
    edges = [('A', 'B'), ('A', 'C'), ('C', 'B'), ('B', 'G'), ('C', 'D'),
             ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H')]
    result = kahn_topological_sort(edges)
    print(result)  # ['A', 'C', 'B', 'D', 'E', 'F', 'G', 'H']
    result = dfs_topological_sort(edges)
    print(result)  # ['A', 'C', 'D', 'E', 'F', 'B', 'G', 'H']
