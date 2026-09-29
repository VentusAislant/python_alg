class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        不能只找一边，因为只找到一边再遍历还是 O(N)复杂度，
        两次，一次找上界，一次找下界即可
        """
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        upper_bound = l - 1

        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        lower_bound = l

        if lower_bound <= upper_bound and upper_bound < len(nums) and nums[lower_bound] == target:
            return [lower_bound, upper_bound]

        return [-1, -1]


if __name__ == '__main__':
    cases = [
        (
            [5, 7, 7, 8, 8, 10], 8,
            [3, 4]
        ),
        (
            [5, 7, 7, 8, 8, 10], 6,
            [-1, -1]
        ),
        (
            [], 0,
            [-1, -1]
        ),
        (
            [1, 3], 1,
            [0, 0]
        ),
    ]
    solution = Solution()
    for case in cases:
        res = solution.searchRange(*case[:-1])
        print(res, case[-1])
