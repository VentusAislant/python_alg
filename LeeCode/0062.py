class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        因为只能向右或者向下走，只需要记录以当前为右下角的路径数量即可
            dp[i][j] : 以 i,j 为右下角的路径数量
            状态转移：
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        """
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return int(dp[m - 1][n - 1])


if __name__ == '__main__':
    cases = [
        (
            3, 7, 28,
        ),
        (
            3, 2, 3
        ),
        (
            7, 3, 28
        ),
        (
            3, 3, 6
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.uniquePaths(*case[:-1])
        print(res, case[-1])
