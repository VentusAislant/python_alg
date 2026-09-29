class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        要求时间复杂度 O(N) 空间复杂度 O(1)
        因为元素要么只出现一次，要么就出现两次，如果出现两次的数能不能通过某种方法抵消?
        目标就是找到一种运算
            a ? a = 0
            0 ? b = b
        异或运算可以满足，因为异或运算满足交换律和结合律，因此
        对于数组 [3, 1, 2, 1, 2]
        3 ^ 1 ^ 2 ^ 1 ^ 2 = 3 ^ (1^1) ^(2^2) = 3 ^ 0 ^ 0 = 3
        直接计算
            3 = 011
            ^1 = 010
            ^2 = 000
            ^1 = 001
            ^2 = 011 = 3
        """
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == '__main__':
    cases = [
        (
            [2, 2, 1],
            1
        ),
        (
            [4, 1, 2, 1, 2],
            4
        ),
        (
            [1],
            1
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.singleNumber(*case[:-1])
        print(res, case[-1])
