"""
最小生成树 (Minimum Spanning Tree, MST): 对于一个带权连通无向图G，
        G的所有生成树（包含所有顶点的极小连通子图）中，权值之和最小的生成树。
1. 普利姆 (Prim) 算法 : 点贪心算法
    从任意一个起点开始，每次选择已访问点与未访问点之间最小权重的边，把新点加入生成树
    可以使用最小堆来维护所有边的权重, 不断从堆中取出所边
2. 克鲁斯卡尔 (Kruskal) 算法: 边贪心算法
    对所有边的权重进行排序，尝试将边加入生成树，如果不会构成环就加入
"""

from collections import defaultdict
import heapq


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False

        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        return True


def mst_kruskal(edges):
    edges.sort(key=lambda x: x[-1])  # 按照权重进行排序
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    size = len(vertices)
    uf = UnionFind(size)

    mst = []
    total_w = 0

    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_w += w
            if len(mst) == size-1:
                break
    return mst, total_w


def mst_prim(edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, u, v))  # # 存三元组 (weight, from, to)
        graph[v].append((w, v, u))

    start = list(graph.keys())[0]
    visited = set([start])
    heap = graph[start][:]  # 使用 [:] 复制一份原始数据，避免原始数据被修改
    heapq.heapify(heap)

    mst = []
    total_w = 0
    while heap and len(visited) < len(graph):
        w, u, v = heapq.heappop(heap)
        if v in visited:
            continue
        else:
            visited.add(v)
            mst.append((u, v, w))
            total_w += w

            # 将 v 的所有边加到堆中
            for edge in graph[v]:
                if edge[2] not in visited:
                    heapq.heappush(heap, edge)
    return mst, total_w


if __name__ == '__main__':
    # 边列表 (u, v, weight)
    """
    0 -- 6-- 2
    | \      |
   10  5     4 
    |    \   |
    1 --15-- 3
    """
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    mst, total_weight = mst_kruskal(edges)
    print("最小生成树边:", mst)
    print("最小生成树总权重:", total_weight)

    mst, total_weight = mst_prim(edges)
    print("最小生成树边:", mst)
    print("最小生成树总权重:", total_weight)

