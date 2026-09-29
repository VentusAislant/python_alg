from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        广度优先遍历思想, 从任意一点出发判断当前是否是一个陆地，可以在原 gird 上直接标记访问过的地方
        如果是则进行广度优先遍历，覆盖尽可能多的陆地，直到访问完全部 gird
        """
        cnt = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # 没访问过的结点
                    # 广度优先遍历
                    queue = deque([(i, j)])
                    grid[i][j] = '2'  # 表示访问过这个结点
                    while queue:
                        cur_i, cur_j = queue.popleft()
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = cur_i + dx, cur_j + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                grid[nx][ny] = '2'
                                queue.append((nx, ny))
                    cnt += 1
        return cnt

    def numIslandsV1(self, grid: list[list[str]]) -> int:
        """
        深度优先遍历
        """

        def dfs(grid, i, j):
            m = len(grid)
            n = len(grid[0])
            grid[i][j] = '2'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    dfs(grid, nx, ny)

        cnt = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # 没访问过的结点
                    cnt += 1
                    dfs(grid, i, j)
        return cnt


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [
                ['1', '1', '1', '1', '0'],
                ['1', '1', '0', '1', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '0', '0', '0']
            ],
            1
        ),
        (
            [
                ['1', '1', '0', '0', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '1', '0', '0'],
                ['0', '0', '0', '1', '1']
            ],
            3
        ),
        (
            [
                ["1", "1", "1"],
                ["0", "1", "0"],
                ["0", "1", "0"]
            ],
            1
        )
    ]
    for case in cases:
        res = solution.numIslandsV1(*case[:-1])
        print(res, case[-1])
