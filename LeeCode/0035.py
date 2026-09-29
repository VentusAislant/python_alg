class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        核心是边界问题，二分查找始终在维持一个正确的区间定义，因为python中都是 左闭右开的，所以初始化
            left = 0  right = len(nums) 代表 [left, right)
            左右子区间分别是 [left, mid), [mid+1, right)
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 4, 2),
    ]
    solution = Solution()
    for case in cases:
        res = solution.searchInsert(*case[:-1])
        print(res, case[-1])
