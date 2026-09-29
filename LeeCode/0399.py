from collections import defaultdict


class Solution:
    def get_path_cost(self, graph, start, end):
        """
        计算从 start 到 end 的路径消耗的乘积，因为要计算表达式的值
            a / c = (a / b) * (b / c)
        params graph: defaultdict(list) 类型
        这里不需要求单源最短路径，理论上两点之间存在路径，所有路径的 cost 都是相同的, 使用深度优先遍历即可
        """

        stack = [(start, 1.0)]  # 当前结点 id 和 当前的累乘值
        seen = {start}

        while stack:
            node, acc = stack.pop()
            for neighbor_id, value in graph[node]:
                prod = acc * value
                if neighbor_id == end:
                    return prod
                if neighbor_id not in seen:
                    seen.add(neighbor_id)
                    stack.append((neighbor_id, prod))

        return -1

    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        """
        可以将 equations 中的变量看作结点，把 queries 中的值看作结点到结点的有向边的权，例如
            equations = [[a,b], [b,c]], values = [2.0, 3.0]
            可以构建如下双向图
                a -> b = 2.0
                b -> a = 0.5
                b -> c = 3.0
                c -> b = 1 / 3.0
            如果要求 a -> c 可以根据链式法则 a -> b -> c = 2.0 * 3.0 = 6.0
        """
        graph = defaultdict(list)
        for equation, value in zip(equations, values):
            var1, var2 = equation
            graph[var1].append((var2, value))
            if value != 0:
                graph[var2].append((var1, 1 / value))

        res = []
        for query in queries:
            var1, var2 = query
            if var1 not in graph or var2 not in graph:
                res.append(-1.0)
                continue

            if var1 == var2:
                res.append(1.0)
            else:
                res.append(self.get_path_cost(graph, var1, var2))
        return res


if __name__ == '__main__':
    sol = Solution()
    cases = [
        (
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            [3.75000, 0.40000, 5.00000, 0.20000]
        ),
        (
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        ),
    ]
    for case in cases:
        res = sol.calcEquation(case[0], case[1], case[2])
        print(res, case[-1])
