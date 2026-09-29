from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        广度优先遍历的轮数，即为橘子腐烂需要的分钟数
        首先需要注意，所有腐烂橘子同时污染周围邻居
        其次需要考虑图有超过一个联通分量的情况
        """
        roted_orange_pos = []  # 腐烂橘子
        orange_pos = []  # 普通橘子
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    roted_orange_pos.append((i, j))
                if grid[i][j] == 1:
                    orange_pos.append((i, j))

        if len(roted_orange_pos) == 0:
            # 没有腐烂橘子
            if len(orange_pos) == 0:
                # 没有橘子
                return 0
            else:
                return -1

        res = 0
        # 广度优先遍历
        queue = deque(roted_orange_pos)
        visited = set(roted_orange_pos)
        new_rotting_oranges = []  # 记录新污染的橘子的位置，用于判断是否全部橘子都污染
        while queue:
            cur_len = len(queue)
            for _ in range(cur_len):
                cur_i, cur_j = queue.popleft()
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = cur_i + di, cur_j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        if (ni, nj) not in visited:
                            visited.add((ni, nj))
                            # 污染相邻的橘子
                            grid[ni][nj] = 2
                            queue.append((ni, nj))
                            new_rotting_oranges.append((ni, nj))

            res += 1

        if len(new_rotting_oranges) < len(orange_pos):
            return -1

        return res - 1


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [[2, 1, 1],
             [1, 1, 0],
             [0, 1, 1]],
            4
        ),
        (
            [[2, 1, 1],
             [0, 1, 1],
             [1, 0, 1]],
            -1
        ),
        (
            [[0, 2]],
            0
        ),

        (
            [[0]],
            0
        )
    ]
    for case in cases:
        res = solution.orangesRotting(*case[:-1])
        print(res, case[-1])
