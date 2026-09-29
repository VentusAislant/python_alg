import math


class Solution:
    def numSquares(self, n: int) -> int:
        """
        1.状态定义
            f(i): 和为 i 的完全平方数的最少数量
        2. 状态转移
            f(i) = min[f(i), f(i-j*j)+1], (for any j, j*j <= i)

        时间复杂度 O(n^1.5)
        空间复杂度 O(n)
        """
        dp = [n] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):  # 降低时间复杂度
                if j * j <= i:
                    dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]

    def numSquaresV1(self, n: int) -> int:
        """
        数学定理：四平方和定理证明了任意一个正证书都可以被表示为至多四个正整数的平方和，也就给出了本题答案的上界
        增强结论：当且仅当 n \neq 4^k \times (8m+7) 时，n 可以表示为至多三个正整数的平方和
        因此我们只会有四种情况：
            res=1， 说明 n 是完全平方数
            res=2， 说明 n=a^2+b^2 枚举所有 a (1<=a<=\sqrt(n)), 判断  n-s^2 是否为完全平方数即可
            res=3,  排除法
            res=4,  n \eq 4^k \times (8m+7)
        """
        if int(math.sqrt(n)) ** 2 == n:
            return 1

        # n =? 4^k * (8m + 7)
        tmp = n
        while tmp % 4 == 0:
            tmp //= 4
        if tmp % 8 == 7:
            return 4

        for a in range(1, int(math.sqrt(n)) + 1):
            x = n - a * a
            if int(math.sqrt(x)) ** 2 == x:
                return 2

        return 3


if __name__ == '__main__':
    cases = [
        (
            12,
            3
        ),
        (
            13,
            2
        ),
        (
            7,
            4
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.numSquaresV1(*case[:-1])
        print(res, case[-1])
