from collections import deque, defaultdict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        """
        首先复制所有结点，构建原始结点到克隆结点的映射表，
        然后根据映射表构建图的边
        """
        if node is None:
            return None

        org2clone = {}

        # 深度优先遍历构建结点
        queue = deque([node])
        seen = {node.val}
        while queue:
            cur_node = queue.popleft()
            org2clone[cur_node.val] = Node(cur_node.val)
            for neighbor in cur_node.neighbors:
                if neighbor.val not in seen:
                    seen.add(neighbor.val)
                    queue.append(neighbor)

        # 深度优先遍历构建边
        queue = deque([node])
        seen = {node.val}
        while queue:
            cur_node = queue.popleft()
            clone_node = org2clone[cur_node.val]
            for neighbor in cur_node.neighbors:
                clone_node.neighbors.append(org2clone[neighbor.val])
                if neighbor.val not in seen:
                    seen.add(neighbor.val)
                    queue.append(neighbor)

        return org2clone[node.val]


def construct_graph(adj_lst: list[list[int]]):
    """
    输入的是 adjList, 如 [[2,4],[1,3],[2,4],[1,3]]
    表示结点 1 有两个相邻结点 [2, 4]
    """
    nodes_dict = {idx + 1: Node(idx + 1) for idx in range(len(adj_lst))}
    for idx, adj in enumerate(adj_lst):
        node = nodes_dict[idx + 1]
        for neighbor in adj:
            node.neighbors.append(nodes_dict[neighbor])
    return nodes_dict[1]


def get_adj_lst(graph):
    """
    传入 graph 获得其 adj_lst
    传入的图的初始结点为 1 所在的结点，结点的值从 1 递增到图的结点个数 size
    """
    if not graph:
        return []

    res = {}
    # 广度优先遍历
    seen = set()
    queue = deque([graph])
    while queue:
        node = queue.popleft()
        seen.add(node.val)
        neighbor_lst = []
        for neighbor in node.neighbors:
            neighbor_lst.append(neighbor.val)
            if neighbor.val not in seen:
                queue.append(neighbor)

        res[node.val] = neighbor_lst

    return [res[k] for k in range(1, len(res) + 1)]


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[2, 4], [1, 3], [2, 4], [1, 3]]
        ),
        (
            [[]],
            [[]]
        ),
    ]
    for case in cases:
        graph = construct_graph(case[0])
        print(graph)
        print(get_adj_lst(graph))
        predict_graph = solution.cloneGraph(graph)
        print(get_adj_lst(predict_graph))
