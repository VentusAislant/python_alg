class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        零钱兑换
            假设 coins = [c1, c2, c3]
            1. 设 dp[i] 表示金额 i 所需要的最少的硬币个数
            2. 兑换金额 i 所需要的最少硬币个数
                dp[i] = min(dp[i-c1], dp[i-c2], dp[i-c3]) + 1
                # 在书写过程中需要 for 遍历所有 coin，不断更新 dp[i] 使其保持最小
                for coin in coins:
                    dp[i] = min(dp[i], dp[i-coin]+1)
            3. 初始化与边界
                dp[i] = inf # 暂时凑不出来
                dp[0] = 0
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                # 尝试将 coin 作为最后一枚
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    cases = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ]
    solution = Solution()
    for case in cases:
        res = solution.coinChange(*case[:-1])
        print(res, case[-1])
