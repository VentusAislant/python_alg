from collections import defaultdict, deque


class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        贪心思想，维护一个最远可到达位置，每次尽可能跳更远
        """
        steps = 0
        cur_end = 0  # 记录当前这一跳最远到达的位置
        farthest = 0  # 下一层能到达的最远距离
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:  # 下一跳
                cur_end = farthest
                steps += 1
        return steps

    def jumpV2(self, nums: list[int]) -> int:
        """
        因为要求的是最少的跳数，因此要尽可能每一步跳得远才行，因此可以逆向思维
            从最后一个位置出发，前一个起跳位置必须是满足要求的距离最远的位置

        时间复杂度: O(N^2) 空间复杂度 O(1)
        615ms 18.36MB
        """
        cur_pos = len(nums) - 1
        steps = 0
        while cur_pos > 0:
            # 从后往前跳，每次找距离最远的起跳点
            for i in range(0, cur_pos):
                if i + nums[i] >= cur_pos:
                    cur_pos = i
                    steps += 1
                    break
        return steps

    def jumpV1(self, nums: list[int]) -> int:
        """
        构建一个图，结点之间存在边表示可达，利用 BFS 求最短路径长度
        时间复杂度 O(N^2) 空间复杂度 O(N^2)
        提交会超时，逻辑正确
        """

        # 构建图
        graph = defaultdict(list)
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                break
            for j in range(i + 1, i + nums[i] + 1):
                graph[i].append(j)

        # 求到最后一个结点的最短路径
        path_length = 0
        queue = deque([0])
        visited = set()
        visited.add(0)
        while queue:
            to_add = []
            while queue:
                cur_node = queue.popleft()
                for neighbor in graph[cur_node]:
                    if neighbor not in visited:
                        if neighbor == len(nums) - 1:
                            return path_length + 1
                        else:
                            to_add.append(neighbor)
            for neighbor in to_add:
                queue.append(neighbor)
            path_length += 1
        return 0


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([2, 0, 0], 1),
        ([2, 0], 1),
        ([2, 0, 1, 0], 2),
        ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], 3),
        ([8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7,
          0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8, 5, 6,
          7, 5, 1, 9, 9, 3, 5, 0, 7, 5], 13),
    ]
    for case in cases:
        r = solution.jump(case[0])
        print(r, case[1])
