class Solution:
    def binary_search(self, nums, x):
        l, r = 0, len(nums)  # [l,r) 左闭右开
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l

    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        贪心 + 二分查找
            如果我们想要上升子序列尽可能长，则需要让序列上升的尽可能慢，
            因此希望每次在上升子序列最后加的那个数尽可能小

            维护一个数组 d[i]，表示长度为 i 的最长上升子序列的末尾元素的最小值，
            用 len 记录目前最长上升子序列的长度

            对于 nums 中的每一个数 x
            1. 在 d 中找第一个 >= x 的位置 pos （d是严格递增的）
            2. 如果找不到 (x 比所有递增子序列的尾元素都大)
                说明可以延长，d.append(x), len+=1
            3. 否则
                需要用 x 替换 d[pos], 可以使得同长度的最长上升子序列结尾更小
        """
        d = []
        for x in nums:
            pos = self.binary_search(d, x)
            if pos == len(d):
                d.append(x)
            else:
                d[pos] = x
        return len(d)

    def lengthOfLISV1(self, nums: list[int]) -> int:
        """
        1. 状态定义非常关键，不能将 dp[i] 定义为前 i 个元素的最长递增子序列长度，因为无法 根据这个信息进行递推
            dp[i] 表示以 nums[i] 结尾的最长递增子序列长度，有末尾元素信息可以进行递推
        2. dp[i] = max(dp[j]+1) 0<=j<i nums[j]<nums[i]
        3. 初始化和边界
            dp[i] = 1, 每个数自己就是一个序列
        """
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:  # 可以添加 nums[j] 到序列中
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ]
    solution = Solution()
    for case in cases:
        res = solution.lengthOfLIS(*case[:-1])
        print(res, case[-1])
