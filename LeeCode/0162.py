class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        O(LogN)解法，因为题目只要求找到任意一个峰值即可，所以可以采用二分查找，
        从中间找，往高的位置走即可， 为什么不会越界
            因为 l < r => mid < r => mid + 1 <= r
        """

        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid + 1] > nums[mid]:
                # 往右边走
                l = mid + 1
            else:
                r = mid
        return l

    def findPeakElementV1(self, nums: list[int]) -> int:
        """
        简单解法：遍历一边如果一个元素值比左右值大即为所求
        时间复杂度为 O(N) 不符合题意
        """
        if len(nums) < 2:
            return 0

        for i in range(len(nums)):
            if i == 0 and nums[i] > nums[i + 1]:
                return i
            elif i == len(nums) - 1 and nums[i] > nums[i - 1]:
                return i
            else:
                if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
                    return i
        return -1


if __name__ == '__main__':
    cases = [
        (
            [1, 2, 3, 1],
            (2,)
        ),
        (
            [1, 2, 1, 3, 5, 6, 4],
            (1, 5)
        ),
        (
            [1, 2],
            (1,)
        ),
    ]
    solution = Solution()
    for case in cases:
        res = solution.findPeakElement(*case[:-1])
        print(res in case[-1], res, case[-1])
