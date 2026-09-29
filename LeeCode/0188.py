class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:

        """
        最多两次交易，变成最多 k 次交易，对应的将原来的变量改成数组即可
            b = [-prices[0]] * k
            s = [0] * k
        总共可能存在的状态
            b[i] 第 i 次买入获得的最大利润
            s[i] 第 s 次卖出后获得的最大利润

        假设今天的价格是 price
            b[0] = max(b[0], -price)
            s[0] = max(s[0], b[0] + price)
            b[1] = max(b[1], s[0] - price)
            s[1] = max(s[1], b[1] + price)
            b[2] = max(b[2], s[1] - price)
            s[2] = max(s[2], b[2] + price)
            ...

        随着不断更新，每个变量都保存了最大的值
        """
        if not prices:
            return 0
        b = [-prices[0]] * k
        s = [0] * k
        for price in prices[1:]:
            b[0] = max(b[0], -price)
            s[0] = max(s[0], b[0] + price)
            for i in range(1, k):
                b[i] = max(b[i], s[i - 1] - price)
                s[i] = max(s[i], b[i] + price)
        return s[-1]


if __name__ == '__main__':
    cases = [
        (
            2, [2, 4, 1],
            2
        ),
        (
            2, [3, 2, 6, 5, 0, 3],
            7
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.maxProfit(*case[:-1])
        print(res, case[-1])
