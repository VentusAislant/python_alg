from collections import deque

"""
对于排列来说，顺序是比较重要的，即使元素相同顺序不同也被认为是一种排列
对于组合来说，顺序不重要，只关心选了哪些元素
"""


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        返回 1-n 中所有可能的 k 个数组合
            先从 start 开始，找到包含 start 所有长度为 k 的 path
            因为组合中重复的元素会被视为一个，所以此时所有包含 start 的元素的组合已经找完，之后应该不考虑这个元素
            可以 start + 1，直接从剩余的元素中继续找组合
        """
        res = []
        path = []

        def backtrack(start):
            if len(path) == k:
                res.append(list(path))
                return

            # 每次都从 start 开始
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return res

    def combineV1(self, n: int, k: int) -> list[list[int]]:
        """
        递归法实现，假设 n = 4, k = 3， 最终结果相当于
            将 n=4 分成两部分，1 和 [2, 3, 4] 结果相当于
                1 和 [2, 3, 4] 中选两个数的组合的拼接 + [2, 3, 4] 中选三个数的组合
            这两部分可以看作，选 1 的组合和不选 1 的组合
            此时可以递归
        """

        def combine_reverse(nums, k):
            if k == 0:
                return [[]]
            if len(nums) < k:  # 不存在组合
                return []
            if len(nums) == k:  # 只存在一个组合即当前所有num构成的列表
                return [nums]

            cur_res = []
            for c in combine_reverse(nums[1:], k - 1):
                cur_res.append([nums[0]] + c)

            cur_res += combine_reverse(nums[1:], k)
            return cur_res

        res = combine_reverse(list(range(1, n + 1)), k)
        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            4, 2,
            [
                [2, 4],
                [3, 4],
                [2, 3],
                [1, 2],
                [1, 3],
                [1, 4],
            ]
        ),
        (
            4, 3,
            [
                [1, 2, 3],
                [1, 2, 4],
                [1, 3, 4],
                [2, 3, 4],
            ]
        ),
        (
            1, 1,
            [[1]]
        )
    ]
    for case in cases:
        res = solution.combineV1(*case[:-1])
        print(res, case[-1])
