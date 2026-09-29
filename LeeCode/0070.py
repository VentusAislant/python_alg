class Solution:
    def climbStairs(self, n: int) -> int:
        """
        设 dp[i] 表示到 第 i 阶的走法数
        递归方程
            dp[i] = dp[i-1] + dp[i-2]
        空间优化版本，因为只依赖前两项，所以只需要两个变量
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b

    def climbStairsV1(self, n: int) -> int:
        """
        设 dp[i] 表示到 第 i 阶的走法数
        递归方程
            dp[i] = dp[i-1] + dp[i-2]
        """
        dp = [-1, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]


if __name__ == '__main__':
    cases = [
        (2, 2),
        (3, 3),
    ]
    solution = Solution()
    for case in cases:
        res = solution.climbStairs(*case[:-1])
        print(res, case[-1])
