class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        设 dp[i] 表示偷窃前 i 个房屋的最高金额
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        dp[i-1] 表示 不偷第 i 个房子，金额等于前 i-1 个房子的最大金额
        dp[i-2] + nums[i] 表示偷第 i 个房子，金额等于前 i-2个房子的最大金额加上 nums[i]

        空间优化
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        a = nums[0]  # 代表 dp[i-2]
        b = max(nums[0], nums[1])  # 代表 dp[i-1]
        for i in range(2, len(nums)):
            cur = max(b, a + nums[i])
            a = b
            b = cur
        return b


    def robV1(self, nums: list[int]) -> int:
        """
        设 dp[i] 表示偷窃前 i 个房屋的最高金额
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        dp[i-1] 表示 不偷第 i 个房子，金额等于前 i-1 个房子的最大金额
        dp[i-2] + nums[i] 表示偷第 i 个房子，金额等于前 i-2个房子的最大金额加上 nums[i]
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
    ]
    solution = Solution()
    for case in cases:
        res = solution.rob(*case[:-1])
        print(res, case[-1])
