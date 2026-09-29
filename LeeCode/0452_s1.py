class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        """
        本质上是求重叠区间的交集数量, 正好和之前求并集相反
        """
        if not points:
            return 0

        points.sort(key=lambda x: x[0])
        stack = [points[0]]
        for i in range(1, len(points)):
            cur_point = points[i]
            if stack[-1][1] >= cur_point[0]:
                # 需要合并
                pop_point = stack.pop()
                right = min(cur_point[1], pop_point[1])
                stack.append([pop_point[0], right])
            else:
                stack.append(cur_point)
        return len(stack)

    def findMinArrowShotsV1(self, points: list[list[int]]) -> int:
        if not points:
            return 0
        # 先按照区间右端升序排列
        points.sort(key=lambda x: x[1])
        arrows = 1  # 记录箭头数量
        cur_pos = points[0][1]  # 记录上个箭头位置
        for i in range(1, len(points)):
            if cur_pos < points[i][0]:  # 如果上个箭头不能打破当前区间的气球
                arrows += 1
                cur_pos = points[i][1]
        return arrows


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2)
    ]
    for case in cases:
        res = solution.findMinArrowShots(*case[:-1])
        print(res, case[-1])

if __name__ == '__main__':
    cases = [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2)
    ]
    solution = Solution()
    for case in cases:
        res = solution.findMinArrowShots(case[0])
        print(res, case[1])
