from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        numCourses 表示需要学习的课程数量， prerequisites 表示课程之间的前后趋关系
        如果没有 prerequisites 则可以学完
        如果 prerequisites 中存在循环依赖则课程无法学完，所以核心是判断一个有向图是否有环
        本质上也是有向图拓扑排序的问题，如果这个有向图能给出拓扑排序，则也能学完所有课程

        拓扑排序思想，每次把入度为 0 的元素放入一个列表，并更新当前的入度信息，重复操作，
        如果最后列表中元素个数小于结点个数，说明存在环
        """
        graph = defaultdict(list)
        in_degree = [0] * numCourses  # 所有课程都初始化入度为0

        for a, b in prerequisites:
            graph[b].append(a)  # 先学 b 才能学 a
            in_degree[a] += 1

        queue = deque()
        for node in range(numCourses):
            if in_degree[node] == 0:
                queue.append(node)

        topological_lst = []
        while queue:
            node = queue.popleft()
            topological_lst.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return len(topological_lst) == numCourses


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            2, [[1, 0]],
            True
        ),
        (
            2, [[1, 0], [0, 1]],
            False
        ),
        (
            5, [[1, 4], [2, 4], [3, 1], [3, 2]],
            True
        )
    ]
    for case in cases:
        res = solution.canFinish(*case[:-1])
        print(res, case[-1])
