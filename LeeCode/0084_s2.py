class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        每个柱子都可以当成最低高度，尽量向左右扩展，形成一个矩形
        关键在于如何高效地确定每个柱子的左右边界
        使用单调递增栈，栈中保存高度递增且还没有遇到右边界的柱子下标
        遍历数组时，如果当前柱子高度小于栈顶柱子，说明栈顶柱子的右边界已经确定，将其弹出
        通过 "当前下标 - 弹出后新栈的栈顶下标 -1" 作为宽度，计算以该柱子为最低高度的最大矩形面积
            [2, 1, 3, 4, 5, 6, 2, 2, 2]
            当计算到下标 1 的时候可以确定前面的最大面积是 2*1=2
            当计算到下标 6 的时候可以确定前面的最大面积是 max(6*1, 5*2, 4*3, 3*4) = 12
            因为在最后 append 了个 0 确保执行完毕，所以
            当计算到下标 9 的时候可以确定前面的最大面积是 max(2*1, 2*2, 2*3, 2*4, 2*5, 2*6, 2*7, 1*8) = 14
        """
        stack = []
        res = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                res = max(res, height * (i - left - 1))
            stack.append(i)

        return res

    def largestRectangleAreaV1(self, heights: list[int]) -> int:
        """
        每个柱子都可以当成最低高度，尽量向左右扩展，形成一个矩形
        简单做法，暴力扩展，找到遇到比自己低的柱子，计算以当前柱子为轴，延伸的矩形的面积
        时间复杂度 O(N^2) 无法通过OJ
        """
        res = 0

        for i in range(len(heights)):
            left, right = i, i
            # 分别向左右扩展
            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            while right <= len(heights) - 1 and heights[right] >= heights[i]:
                right += 1

            left += 1
            right -= 1
            res = max(res, heights[i] * (right - left + 1))

        return res


if __name__ == '__main__':
    cases = [
        (
            [2, 1, 5, 6, 2, 3], 10
        ),
        (
            [2, 1, 3, 4, 5, 6, 2, 3], 12
        ),
        (
            [2, 1, 3, 4, 5, 6, 2, 2, 2], 14
        ),
        (
            [2, 4], 4
        ),

        (
            [2, 1, 2], 3
        )
    ]

    solution = Solution()
    for case in cases:
        res = solution.largestRectangleArea(*case[:-1])
        print(res, case[-1])
