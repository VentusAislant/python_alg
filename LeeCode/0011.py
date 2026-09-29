from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        从两端向中间遍历, 每次只把高度比较低的指针进行移动，来确保下一个可能获得更多区域
        """
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            h = min(height[i], height[j])
            max_area = max(max_area, h * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == '__main__':
    cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1)
    ]
    solution = Solution()
    for case in cases:
        result = solution.maxArea(case[0])
        print(result, case[1])
