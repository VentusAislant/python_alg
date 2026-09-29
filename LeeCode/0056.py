class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        首先按照左边界进行升序排序，排序后判断重叠规则较为容易
            如果前者的右边界大于等于后者的左边界，说明存在重叠，需要将两者合并
            利用一个栈来存储最终的合并完毕的区间
        """
        if not intervals: return []
        intervals.sort(key=lambda x: x[0])
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            if stack[-1][1] >= intervals[i][0]:
                pop_element = stack.pop()
                left = min(intervals[i][0], pop_element[0])
                right = max(intervals[i][1], pop_element[1])
                stack.append([left, right])
            else:
                stack.append(intervals[i])
        return stack

if __name__ == '__main__':
    cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
    ]
    solution = Solution()
    for case in cases:
        res = solution.merge(case[0])
        print(res, case[1])
