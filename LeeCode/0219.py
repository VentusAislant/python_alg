class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        暴力解法的可以分为两步，第一步枚举一个索引 i, 第二步枚举 索引 j!= i 判断是否满足条件
        我们可以用空间换时间，nums 中有重复元素，我们要找的是距离最近的两个重复元素，所以可以用
        一个哈希表存储最近一次出现的 num 及其索引，来获得最近的距离
        """
        last_num2idx = {}
        for i in range(len(nums)):
            if nums[i] in last_num2idx and abs(i - last_num2idx[nums[i]]) <= k:
                return True
            last_num2idx[nums[i]] = i
        return False

    def containsNearbyDuplicateV1(self, nums: list[int], k: int) -> bool:
        """
        暴力解法，枚举所有 i 和 j 二元组，判断是否满足条件
        时间复杂度 O(n^2)  会超时
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] == nums[j] and abs(i - j) <= k:
                        return True
        return False


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
        ([0, 1, 2, 3, 4, 0, 0, 7, 8, 9, 10, 11, 12, 0], 1, True),
    ]
    solution = Solution()
    for case in cases:
        res = solution.containsNearbyDuplicate(case[0], case[1])
        print(res, case[2])
