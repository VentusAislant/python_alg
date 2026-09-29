class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        动态规划
        因为可以在任意时刻买卖，但是同时只能持有一只股票，因此只有两个状态
            buy： 手里持有股票时的最大利润
            sell: 手里没有股票时的最大利润
        状态转移：
            对于今天价格 price
            buy = max(
                buy,  # 昨天已经持股，今天不动
                sell - price  # 今天买入
            )

            sell = max(
                sell, # 昨天已经卖出，今天不动
                buy + price  # 今天卖出
            )

        """
        b = -prices[0]
        s = 0
        for price in prices[1:]:
            b = max(b, s - price)
            s = max(s, b + price)
        return s

    def is_minimum(self, prices: list[int], index) -> bool:
        if index == 0:
            return prices[0] < prices[1]
        elif index == len(prices) - 1:
            return prices[index] < prices[index - 1]
        else:
            return prices[index] <= prices[index + 1] and prices[index] <= prices[index - 1]

    def is_maximum(self, prices: list[int], index) -> bool:
        if index == 0:
            return prices[0] > prices[1]
        elif index == len(prices) - 1:
            return prices[index] > prices[index - 1]
        else:
            return prices[index] >= prices[index + 1] and prices[index] >= prices[index - 1]

    def maxProfitV1(self, prices: list[int]) -> int:
        """
        以极小值点买入，在下一个极大值点卖出
        时间复杂度 O(N)
        空间复杂度 O(1)
        """
        if len(prices) < 2:
            return 0
        s = 0  # 信号量，表示需要极大值的数量
        total_profits = 0
        cur_minimum = float('inf')
        for i in range(len(prices)):
            if self.is_minimum(prices, i):
                s += 1  # 供应一个极大值需求量
                cur_minimum = prices[i]
            if s > 0 and self.is_maximum(prices, i):
                s -= 1  # 消费一个极大值需求量
                total_profits += prices[i] - cur_minimum
        return total_profits


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([3, 3, 5, 0, 0, 3, 1, 4], 8)
    ]
    for case in cases:
        r = solution.maxProfit(case[0])
        print(r, case[1])
