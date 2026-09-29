class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # 每个节点自成一个集合
        self.rank = [0] * size  # 每个节点树高初始为0

    def union(self, x, y):
        root_x = self.find_root(x)
        root_y = self.find_root(y)
        if root_x == root_y:
            return False  # x 和 y 已经在同一个集合中

        # 根据节点高度合并
        if self.rank[root_x] > self.rank[root_y]:
            # 树高比较低的作为子节点不会增加树的层数，加快检索效率
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1
        return True

    def find_root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]


def have_cycle(vertices: list | tuple, edges: list | tuple) -> bool:
    """
    使用并查集，判断一个无向图是否有环
    :param vertices: 顶点集合
    :param edges: 边的集合
    :return: 是否有环
    """
    uf = UnionFind(len(vertices))
    for e in edges:
        if not uf.union(e[0], e[1]):
            # 有环
            return True
    return False


if __name__ == '__main__':
    vertices = [0, 1, 2, 3]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]  # 形成 0-1-2-3-0 的环
    print(have_cycle(vertices, edges))  # 输出 True

    edges2 = [(0, 1), (1, 2), (2, 3)]  # 无环
    print(have_cycle(vertices, edges2))  # 输出 False
