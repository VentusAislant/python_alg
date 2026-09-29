class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        由于区间数组已经有序，可以先根据 start 查到当前新区间在原来区间数组中的预期位置，
        然后执行合并
        """
        if not intervals:
            return [newInterval]

        insert_pos = len(intervals)  # 默认在表尾插入
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                insert_pos = i
                break
        intervals.insert(insert_pos, newInterval)

        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            if stack[-1][1] >= cur_interval[0]:
                pop_element = stack.pop()
                left = min(cur_interval[0], pop_element[0])
                right = max(cur_interval[1], pop_element[1])
                stack.append([left, right])
            else:
                stack.append(cur_interval)
        return stack


if __name__ == '__main__':
    cases = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ([[1, 5]], [2, 3], [[1, 5]]),
        ([], [2, 3], [[2, 3]]),
        ([[1, 5]], [1, 7], [[1, 7]]),
        ([[1, 5]], [0, 3], [[0, 5]]),
    ]
    solution = Solution()
    for case in cases:
        res = solution.insert(case[0], case[1])
        print(res, case[2])
