class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        因为子集不要求连续，所以按顺序遍历很难划分子集，可以换一个视角
        什么时候肯定不能分？  -> 和为奇数的时候肯定无法划分
        什么时候能分？ 和为偶数的时候，并且肯定能找到一个子集和为 sum//2，
        此时划分子集就变成了找一个和为 sum//2的子集的过程
            也就转化成了 01 背包问题
            dp[i]: 是否能用前若干个数凑出和 i
            i 是背包容量，dp[i] 是布尔值
            dp[0] = True 什么都不选可以凑出 0
            dp[i] = dp[i] or dp[i-num]
        """
        sum_all = sum(nums)
        if sum_all % 2 == 0:
            target = sum_all // 2
            dp = [False] * (target + 1)
            dp[0] = True
            for num in nums:
                for i in range(target, num - 1, -1):
                    dp[i] = dp[i] or dp[i - num]
            return dp[target]
        return False


if __name__ == '__main__':
    cases = [
        (
            [1, 5, 11, 5],
            True
        ),
        (
            [1, 2, 3, 5],
            False
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.canPartition(case[0])
        print(res, case[-1])
