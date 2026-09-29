class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        """
        1. 状态定义
            f(i,j) 表示以 i, j 为右下角的，全是 1 的最大正方形边长
        2. 初始化
            对于第一行或第一列的值，当前值为 1, f值也为1

        3. 状态转移
            左上: f(i-1, j-1)
            上: f(i-1, j)
            左: f(i, j-1)
            如果当前位置是 0, matrix[i][j] == 0:
                f(i, j) = 0  以这个位置为右下角没有矩形
            如果当前位置是 1， 则想是否能够扩展边长， 需要每个方向都能贡献边长，找出每个方向都能贡献的边长
            类似木桶找短板
                f(i, j) = min(
                    f(i-1, j-1),
                    f(i-1, j),
                    f(i, j-1)
                ) + 1
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        max_len = 0
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
            if dp[i][0] > max_len:
                max_len = dp[i][0]
        for j in range(1, n):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
            if dp[0][j] > max_len:
                max_len = dp[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1]
                    ) + 1

                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
        return max_len * max_len


if __name__ == '__main__':
    cases = [
        (
            [["1", "0", "1", "0", "0"],
             ["1", "0", "1", "1", "1"],
             ["1", "1", "1", "1", "1"],
             ["1", "0", "0", "1", "0"]],
            4
        ),
        (
            [["0", "1"], ["1", "0"]],
            1
        ),
        (
            [["0"]],
            0
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.maximalSquare(*case[:-1])
        print(res, case[-1])
