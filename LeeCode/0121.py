class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        动态规划
            b 表示当前购买获得的最大利润
            s 表示当前售出获得的最大利润
        状态转移
        对于当天价格 price
            b = max(b, -price)  之前就买或者现在买
            s = max(s, s-price)  之前就卖出，或者现在卖
        """
        b = -prices[0]
        s = 0
        for price in prices[1:]:
            b = max(b, -price)
            s = max(s, b + price)
        return s


    def maxProfitV2(self, prices: list[int]) -> int:
        """
        最大利润的关键是两件事：
            记录到目前为止出现的最低价格
            记录 当前价格 - 最大价格能获得的最大利润
        """
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            cur_profit = price - min_price
            if cur_profit > max_profit:
                max_profit = cur_profit
        return max_profit


    def maxProfitV1(self, prices: list[int]) -> int:
        """
        暴力解法， O(n^2)
        """
        cur_max_profit = 0
        n = len(prices)
        for i in range(0, n):
            for j in range(i, n):
                profit = prices[j] - prices[i]
                if cur_max_profit < profit:
                    cur_max_profit = profit
        return cur_max_profit


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0)
    ]
    for case in cases:
        r1 = solution.maxProfit(case[0])
        r2 = solution.maxProfit(case[0])
        print(r1, r2, case[1])
