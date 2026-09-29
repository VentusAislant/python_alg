class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        最简单的做法是检索任意起点 [0, n-1] 所有窗口大小 [1, n] 中是否有满足条件的
            时间复杂度 O(N^2)

        改进1：暴力解法中全部遍历没有必要，因为数组长度越长值越大，可以用二分查找来搜索窗口大小
            时间复杂度 O(N * logN)

        改进做法：滑动窗口，因为数组中所有的数都是正整数
            1. 左右指针构成一个窗口
            2. 窗口右边界右移 -> 子数组和会增大
            3. 窗口左边界右移 -> 子数组和会减少

        因此可以维护一个动态窗口，当窗口内的和大于等于 target 时，尽可能缩小窗口，并记录窗口程度
        整个过程只需要左右指针最多遍历一边数组，所以时间复杂度 O(N), 空间复杂度 O(1)
        """
        res = float('inf')
        left = 0
        window_sum = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                # 可以收缩左边界了
                res = min(res, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if res == float('inf') else res



if __name__ == '__main__':
    solution = Solution()
    cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0)
    ]
    for case in cases:
        result = solution.minSubArrayLen(case[0], case[1])
        print(result, case[2])
