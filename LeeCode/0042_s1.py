class Solution:
    def trap(self, height: list[int]) -> int:
        """
        标准的双指针解法
            左指针 left 只能向右移动，右指针 right 只能向左移动
            left_max 记录目前左侧的最高柱， right_max 记录目前右侧最高柱子
            每个位置能装的水量 = min(left_max, right_max) - height[i]
        """
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        while left < right:
            if height[left] > height[right]:
                # 当前左侧更高，先填充墙比较低的右侧的水
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
            else:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
        return res

    def trapV1(self, height: list[int]) -> int:
        """
        首先假设最右侧有个无限高的挡板，从左至右计算可接水面积 s_left
        再假设左侧有个无限高的挡板，从右往左计算可接水面积 s_right
        假设所有墙的面积为 s_wall, 整个空间的面积为 s_all = max(height) * len(height)
        设可接水面积为 res
        可以发现 s_all = s_left + s_right + s_wall - res
        所以 res = s_left + s_right + s_wall - s_all

        时间复杂度 O(N), 空间复杂度 O(1)
        """
        s_left, s_right, s_wall = 0, 0, 0
        s_all = max(height) * len(height)

        cur_max = 0
        for i in range(len(height)):
            if height[i] > cur_max:
                cur_max = height[i]
            else:
                s_left += cur_max - height[i]

            s_wall += height[i]

        cur_max = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > cur_max:
                cur_max = height[i]
            else:
                s_right += cur_max - height[i]

        return s_left + s_right + s_wall - s_all


if __name__ == '__main__':
    cases = [
        (
            [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
            6
        ),
        (
            [4, 2, 0, 3, 2, 5],
            9
        ),
        (
            [5, 4, 1, 2],
            1
        ),
        (
            [0, 5, 0, 3, 0, 5, 0],
            12
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.trap(case[0])
        print(res, case[1])
