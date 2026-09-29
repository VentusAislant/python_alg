class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """
        可以分两种情况
            第一种情况最大连续子数组在原数组中间位置，则和原来的解法一样
            第二种情况，最大连续子数组起点在右侧，终点在左侧, 这个可以用逆向思维
                此时的 最大连续子数组和 = 总和 - 最小连续子数组和
                因为只需要在中间挖掉一段不需要的即可，这个不需要的要尽可能小，例如
                [1, 2, 3, -1, -2, -3, 4, 5, 6]
                只需要挖掉中间的负数即可
        """
        total_sum = sum(nums)

        max_sum = nums[0]
        cur_max = nums[0]
        min_sum = nums[0]
        cur_min = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i] + cur_max, nums[i])
            max_sum = max(max_sum, cur_max)

            cur_min = min(nums[i] + cur_min, nums[i])
            min_sum = min(min_sum, cur_min)

        if max_sum < 0:
            # 说明数组均为负数
            return max_sum

        return max(max_sum, total_sum - min_sum)


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [1, -2, 3, -2],
            3
        ),
        (
            [5, -3, 5],
            10
        ),
        (
            [3, -2, 2, -3],
            3
        )
    ]
    for case in cases:
        res = solution.maxSubarraySumCircular(*case[:-1])
        print(res, case[-1])
