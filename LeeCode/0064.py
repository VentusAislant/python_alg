class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        1. 状态定义：
            用二维数组 dp[i][j] 定义到 grid[i][j] 的最小路径和
        2. 状态转移：
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])+ grid[i][j]
            上一步只可能来自左边或上边
        3. 初始化与边界
            dp[i][j] = inf
            dp[0][0] = grid[0][0]
        """
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return int(dp[m-1][n-1])


if __name__ == '__main__':
    cases = [
        (
            [[1, 3, 1],
             [1, 5, 1],
             [4, 2, 1]],
            7
        ),
        (
            [[1, 2, 3],
             [4, 5, 6]],
            12
        ),
        (
            [[1, 3],
             [1, 5]],
            7
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.minPathSum(*case[:-1])
        print(res, case[-1])
