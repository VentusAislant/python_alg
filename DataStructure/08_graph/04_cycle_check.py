from collections import deque, defaultdict

class UnionFind:
    def __init__(self, size):
        self.size = size
        self.parents = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            return self.find(self.parents[x])

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.parents[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parents[root_x] = root_y
        else:
            self.parents[root_x] = root_y
            self.rank[root_y] += 1
        return True



def hava_cycle(edges) -> bool:
    """
    使用并查集来判断一个图，是否有环
    :param edges: 边的集合
    :return: 是否有环
    """
    size_set = set()
    for u, v in edges:
        size_set.add(u)
        size_set.add(v)
    size = len(size_set)
    uf = UnionFind(size)
    for u, v in edges:
        if not uf.union(u, v):
            return True
    return False


def have_cycle2(edges) -> bool:
    """
    使用深度优先遍历
    :param edges:
    :return:
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(cur_node, parent=None):
        visited.add(cur_node)
        for neighbor in graph[cur_node]:
            if neighbor not in visited:
                # 如果有任意一个 neighbor 判断有环，则直接返回True即可
                if dfs(neighbor, cur_node):
                    return True
            elif parent is not None and neighbor != parent:
                return True
        return False

    # 防止有多个连通分量
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False


if __name__ == '__main__':
    edges = [(0, 1), (1, 2), (2, 3), (2, 0)]
    print(hava_cycle(edges))
    print(have_cycle2(edges))

    edges = [(0, 1), (1, 2), (2, 3)]
    print(hava_cycle(edges))
    print(have_cycle2(edges))