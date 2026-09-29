class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        贪心算法：
            每走一步计算当前能到达的最远的位置
            60ms 18.41MB
        """
        max_reach = nums[0]
        for i in range(1, len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True

    def canJumpV1(self, nums: list[int]) -> bool:
        """
        贪心算法：
            每走一步计算当前能到达的最远的位置
            27ms 18.36MB
        """
        target_pos = len(nums) - 1
        max_jump_pos = min(nums[0], target_pos)

        i = 1
        while i <= max_jump_pos:
            if max_jump_pos >= target_pos:
                return True

            if i + nums[i] > max_jump_pos:
                max_jump_pos = min(i + nums[i], target_pos)

            i += 1

        if max_jump_pos < target_pos:
            return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([1, 0, 2], False),
        ([2, 0, 0], True),
        ([2, 0], True),
        ([2, 0, 1, 0], True),
        ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], True),
    ]
    for case in cases:
        r = solution.canJumpV1(case[0])
        print(r, case[1])
