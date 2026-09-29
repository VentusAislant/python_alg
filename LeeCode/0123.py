class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        总共可能存在的状态
            0: 什么都没做
            1: 第一次买入
            2: 第一次卖出
            3: 第二次买入
            4: 第二次卖出
        以上状态按顺序执行，可以用四个变量，记录四个状态下的最大利润
            b1: 第一次买入后的最大利润
            s1: 第一次卖出后的最大利润
            b2: 第二次买入后的最大利润
            s2: 第二次卖出后的最大利润

        假设今天的价格是 price
            对于第一次买入后的最大利润
                b1 = max(b1, -price)  # 之前买的情况，和现在买，用负数因为是购买，price越大，b1越少
            对于第一次卖出后的最大利润
                s1 = max(s1, b1+price)  # 之前已经卖了或者现在卖
            对于 b2:
                b2 = max(b2, s1 - price)  # 之前已经第二次买了，还是现在买
            对于 s2:
                s2 = max(s2, b2+price)  # 之前已经买了和现在卖

        随着不断更新，每个变量都保存了最大的值
        """
        if not prices:
            return 0
        b1 = -prices[0]
        s1 = 0
        b2 = -prices[0]
        s2 = 0
        for price in prices[1:]:
            b1 = max(b1, -price)
            s1 = max(s1, b1 + price)
            b2 = max(b2, s1 - price)
            s2 = max(s2, b2 + price)
        return s2


if __name__ == '__main__':
    cases = [
        (
            [3, 3, 5, 0, 0, 3, 1, 4],
            6
        ),
        (
            [1, 2, 3, 4, 5],
            4
        ),
        (
            [7, 6, 4, 3, 1],
            0
        ),
        (
            [1],
            0
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.maxProfit(*case[:-1])
        print(res, case[-1])
