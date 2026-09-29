class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        题目中难点在相邻的两个孩子中，评分高的获得更多的糖果
            相邻是双向的，所以可以两次扫描，左侧和右侧得到最终结果
            首先每个孩子一个糖果，然后分别从左侧右侧补发
            左侧：
                如果 ratings[i] > ratings[i-1]:
                    candies[i] = candies[i-1] + 1
                否则交给右侧处理
            右侧：
                如果 ratings[i] > ratings[i+1]:
                    candies[i] = max(candies[i], candies[i+1] + 1)
                    使用 max 因为经过左侧遍历可能当前的糖果数量足够多了，不会被右侧的更小值覆盖

        时间复杂度 O(N), 空间复杂度 O(N)
        """
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # range 包含 start 不包含 end
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)


if __name__ == '__main__':
    cases = [
        (
            [1, 0, 2],
            5
        ),
        (
            [1, 2, 2],
            4
        ),
        (
            [1, 2, 3, 2, 0],
            9
        ),
        (
            [3, 2, 1, 2, 3],
            11
        ),
        (
            [1, 3, 4, 5, 2],
            11
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.candy(case[0])
        print(res, case[1])
