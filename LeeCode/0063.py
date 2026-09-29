class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        """
        1. 状态定义：
            用二维数组 dp[i][j] 定义总 grid[0][0] 到 grid[i][j] 的不同路径数量
        2. 状态转移：
            dp[i][j] = dp[i-1][j] + dp[i][j-1] (注意边界情况)
            上一步只可能来自左边或上边
            还需要注意的是 如果 obstacleGrid[i][j] == 1 则 dp[i][j] = 0
        3. 初始化与边界
            dp[0][0] = 1
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


if __name__ == '__main__':
    cases = [
        (
            [[0, 0, 0],
             [0, 1, 0],
             [0, 0, 0]],
            2
        ),
        (
            [[0, 1],
             [0, 0]],
            1
        ),
        (
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]],
            6
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.uniquePathsWithObstacles(*case[:-1])
        print(res, case[-1])
