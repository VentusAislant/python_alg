class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        因为数组预先旋转了 k 位，当 k > 0 时，数组可以分为两段升序的数组，
        对于任意一个 mid，肯定会至少存在一边是有序的,
            对于有序的数组，可以根据左右断点，判断当前 target 是否在其范围内
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1

            if nums[mid] == target:
                return mid

            # 左半边 [l, mid-1] 有序
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 右半边 [mid+1, r] 有序
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


if __name__ == '__main__':
    cases = [
        (
            [4, 5, 6, 7, 0, 1, 2], 0,
            4
        ),
        (
            [4, 5, 6, 7, 0, 1, 2], 3,
            -1
        ),
        (
            [4, 5, 6, 7, 0, 1, 2], 4,
            0
        ),
        (
            [1], 0,
            -1
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.search(*case[:-1])
        print(res, case[-1])
