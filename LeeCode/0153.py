class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        旋转排序数组，可以用二分查找，核心是保证最小值在 [l, r] 中即可

        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[r]:
                # 说明最小值在右端，因为中间值大于右端点只有在旋转 k 次， k < n 时出现
                l = mid + 1
            else:
                r = mid
        return nums[l]


if __name__ == '__main__':
    cases = [
        (
            [3, 4, 5, 1, 2], 1
        ),
        (
            [4, 5, 6, 7, 0, 1, 2], 0
        ),
        (
            [11, 13, 15, 17], 11
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.findMin(*case[:-1])
        print(res, case[-1])
