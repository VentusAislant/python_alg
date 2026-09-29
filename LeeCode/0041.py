class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        """
        假设数组长度为 n，那么缺失的第一个正数必然在 [1,n+1] 之间
        而整个数组的索引范围恰好是 [0, n-1] 和前面的范围仅仅差最后一个数
        可以把数组本身当作一个哈希表，第 i 个位置只能存放 i+1 这个数
        负数，0，或者大于 n 的数都不用管，最后重头看一遍数组，第 i 个位置上 不是 i+1 也就是这个数缺失
        """
        n = len(nums)
        i = 0
        while i < n:
            x = nums[i]
            if 1 <= x <= n and nums[x - 1] != x:
                nums[i], nums[x - 1] = nums[x - 1], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

    def firstMissingPositiveV1(self, nums: list[int]) -> int:
        """
        先排序，然后依次检查，直到那个缺失的正数
        时间复杂度 O(NlogN)  不满足题目要求的 O(n) 时间复杂度
        """
        nums.sort()
        pre = 0
        for num in nums:
            if num > 0:
                if num > pre + 1:
                    return pre + 1
                else:
                    pre = num
        return pre + 1


if __name__ == '__main__':
    cases = [
        (
            [1, 2, 0, 1, 2], 3
        ),
        (
            [1, 2, 0], 3
        ),
        (
            [3, 4, -1, 1], 2
        ),
        (
            [7, 8, 9, 11, 12], 1
        )
    ]

    solution = Solution()
    for case in cases:
        res = solution.firstMissingPositive(*case[:-1])
        print(res, case[-1])
