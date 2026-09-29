from collections import defaultdict


class Solution:

    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        前缀和思想
            设 pre_sum[i] = nums[0] + ... + nums[i]
            我们要找到子数组和为 k, 只需要在位置 j 找到之前有多少个 i 满足
                pre_sum[j] - pre_sum[i] == k
            即可
        能否优化时间
            能否不用双重循环，j不动，每次都在判断前面有多少个前缀和等于 pre_sum[j] - k
            可以用一个哈希表记录前面的前缀和到出现次数的对应
            此外可以一边计算前缀和，一边遍历，无需两个 for
        """
        cnt = defaultdict(int)  # 记录前面的前缀和及其出现次数
        cnt[0] = 1  # 在还没开始之前，前缀和 0 出现过一次
        cur_sum = 0
        res = 0
        for num in nums:
            cur_sum += num
            res += cnt[cur_sum - k]
            cnt[cur_sum] += 1
        return res

    def subarraySumV1(self, nums: list[int], k: int) -> int:
        """
        前缀和思想
            设 pre_sum[i] = nums[0] + ... + nums[i]
            我们要找到子数组和为 k, 只需要在位置 j 找到之前有多少个 i 满足
                pre_sum[j] - pre_sum[i] == k
            即可
        时间复杂度 O(N^2)
        """
        pre_sum = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            pre_sum.append(cur_sum)

        res = 0
        for j in range(len(pre_sum)):
            if pre_sum[j] == k:
                res += 1
            for i in range(j):
                if pre_sum[j] - pre_sum[i] == k:
                    res += 1

        return res


if __name__ == '__main__':
    test_cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2)
    ]
    s = Solution()

    for case in test_cases:
        my_answer = s.subarraySum(*case[:-1])
        print(my_answer, " | ", case[-1])
