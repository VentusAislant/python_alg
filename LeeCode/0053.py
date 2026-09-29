class Status:
    def __init__(self, l_sum, r_sum, m_sum, i_sum):
        self.l_sum = l_sum
        self.r_sum = r_sum
        self.m_sum = m_sum
        self.i_sum = i_sum


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        分治算法：
            将 nums 递归进行左右两个区间 [l, m], [m+1, r] 的最大连续子数组和
            递归是如何利用左右区间信息计算整个区间信息比较关键
                l_sum 记录 以 l 为左端点的最大连续子数组和
                r_sum 记录 以 r 为右端点的最大连续子数组和
                m_sum 记录 [l, r] 内的最大连续子数组和
                i_sum 记录 [l, r] 的区间和

            对于整个区间来说
                i_sum 等于左子区间的 i_sum + 右子区间的 i_sum
                l_sum 要么等于左子区间的 l_sum, 要么等于左子区间的 i_sum + 右子区间的 l_sum
                r_sum 要么等于右子区间的 r_sum, 要么等于右子区间的 i_sum + 左子区间的 r_sum
                m_sum:
                    如果最大连续子数组不跨越 m, 则 m_sum = max(左子区间的 m_sum, 右子区间的 m_sum)
                    否则 m_sum = max(左子区间的 m_sum, 右子区间的 m_sum, 左子区间的 r_sum+右子区间的 l_sum)
        """

        def divide(nums, l, r) -> Status:
            if l == r:
                return Status(nums[l], nums[l], nums[l], nums[l])

            m = (l + r) >> 1  # 中点
            l_status = divide(nums, l, m)
            r_status = divide(nums, m + 1, r)

            i_sum = l_status.i_sum + r_status.i_sum
            l_sum = max(l_status.l_sum, l_status.i_sum + r_status.l_sum)
            r_sum = max(r_status.r_sum, r_status.i_sum + l_status.r_sum)
            m_sum = max(max(l_status.m_sum, r_status.m_sum), l_status.r_sum + r_status.l_sum)
            return Status(l_sum, r_sum, m_sum, i_sum)

        return divide(nums, 0, len(nums) - 1).m_sum

    def maxSubArrayV2(self, nums: list[int]) -> int:
        """
        基于 V1 版本可以不使用 O(N) 空间，直接用一个 pre 变量记录以前一个位置结尾的连续子数组的最大和即可
        """
        pre = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            cur = max(pre + nums[i], nums[i])
            pre = cur
            if cur > res:
                res = cur
        return res

    def maxSubArrayV1(self, nums: list[int]) -> int:
        """
        动态规划：
            假设 f(i) 代表以第 i 个数结尾的连续子数组的最大和，然后返回最大的 f(i) 即可
            f(i) = max{f(i-1) + nums[i], nums[i]}
        """
        dp = [nums[0]]
        res = nums[0]
        for i in range(1, len(nums)):
            cur = max(dp[i - 1] + nums[i], nums[i])
            if cur > res:
                res = cur
            dp.append(cur)
        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            6
        ),
        (
            [1],
            1
        ),
        (
            [5, 4, -1, 7, 8],
            23
        )
    ]
    for case in cases:
        res = solution.maxSubArray(*case[:-1])
        print(res, case[-1])
