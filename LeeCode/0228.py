class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        """
        使用 left 指针记录当前子区间左边界， right 指针记录当前子区间右边界
            当区间连续不断右移动 right
            遇到不连续的地方，先将 [left, right] 放到结果列表，然后
                left = right
        """
        left, right = 0, 0
        res = []
        while right < len(nums):
            if right + 1 < len(nums) and nums[right] + 1 == nums[right + 1]:
                # 目前还是连续
                right += 1
            else:
                to_append = str(nums[left]) if nums[left] == nums[right] else f"{nums[left]}->{nums[right]}"
                res.append(to_append)
                left = right + 1
                right = left
        return res


if __name__ == '__main__':
    cases = [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    ]
    solution = Solution()
    for case in cases:
        res = solution.summaryRanges(case[0])
        print(res, case[1])
