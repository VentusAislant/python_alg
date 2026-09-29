class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        基于 V1 版本优化，不需要 O(n) 空间，因为只以来前一位状态来更新
        """
        cur_max = cur_min = res = nums[0]
        for i in range(1, len(nums)):
            tmp_max, tmp_min = cur_max, cur_min
            cur_max = max(nums[i], tmp_max * nums[i], tmp_min * nums[i])
            cur_min = min(nums[i], tmp_max * nums[i], tmp_min * nums[i])
            if cur_max > res:
                res = cur_max
        return res

    def maxProductV1(self, nums: list[int]) -> int:
        """
        1.状态定义
            f(i): 以 nums[i] 结尾的最大非空连续子数组所对应的乘积
            关键是怎么应对负数
            所以还需要记录一个最小值乘积
            g(i): 以 nums[i] 结尾的最小非空连续子数组所对应的乘积
        2. 状态转移
            f(0) = nums[0], g(0) = nums[0]

            对于 i
            f(i) = max(nums[i], f(i)*nums[i], g(i)*nums[i])
            g(i) = min(nums[i], f(i)*nums[i], g(i)*nums[i])

        时间复杂度 O(n)
        空间复杂度 O(2n)
        nums = [2, 3, -5, -6, 3 ,2]
        f = [2, 6, -5, 180, 540, 1080]
        j = [2, 3, -30, -6, -18, -36]
        """
        f = [nums[0]] * len(nums)
        j = [nums[0]] * len(nums)
        res = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(nums[i], f[i - 1] * nums[i], j[i - 1] * nums[i])
            j[i] = min(nums[i], j[i - 1] * nums[i], f[i - 1] * nums[i])
            if f[i] > res:
                res = f[i]
        return res


if __name__ == '__main__':
    cases = [
        (
            [2, 3, -2, 4],
            6
        ),
        (
            [-2, 0, -1],
            0
        ),
        (
            [2, 3, -5, -6, 3, 2],
            1080
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.maxProduct(*case[:-1])
        print(res, case[-1])
