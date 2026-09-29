from collections import defaultdict

"""
`defaultdict` 是 `dict` 的一个子类
    可以在访问不存在的键时自动创建并赋一个默认值，而不用判断键是否存在
    传入一个类型参数，如果传入 list 则默认构建一个 list
"""

# 邻接表方式构建无向图
graph = defaultdict(list)
edges = ((0, 1), (1, 2), (2, 0))
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
print(graph)
