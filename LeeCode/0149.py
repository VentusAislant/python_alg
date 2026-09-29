class Solution:
    def gcd(self, a, b):
        return self.gcd(b, a % b) if b else a

    def maxPoints(self, points: list[list[int]]) -> int:
        """
        在坐标系中直线可以表示为 y=kx，所以一条直线仅仅对应一个 k
        维护一个 res 变量，记录最多点个数
        可以一个点为基准，遍历所有以这个点出发的可能的两点构成的线，记录每个线上的点的个数
        不同点为基准是，记录最大点个数
        """
        n = len(points)
        if n <= 2:
            return n
        res = 0
        for i in range(n):
            cnt_map = {}
            for j in range(i + 1, n):  # 这样可以遍历不重复的点对
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == 0:
                    k = (0, points[i][1])
                elif dy == 0:
                    k = (points[i][0], 0)
                else:
                    # 直接用精准数值斜率可能会导致数值偏差，影响结果，这里可以采用约分后的分数作为 k
                    if dy < 0:
                        dx = -dx
                        dy = -dy

                    g = self.gcd(abs(dx), abs(dy))
                    k = (dx // g, dy // g)

                if k not in cnt_map:
                    cnt_map[k] = 2  # 加入当前的两个点
                else:
                    cnt_map[k] += 1  # 只加入新的点

            cur_res = 0
            for k, v in cnt_map.items():
                if v > cur_res:
                    cur_res = v

            if cur_res > res:
                res = cur_res
        return res


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([[1, 1], [2, 2], [3, 3]], 3),
        ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
        ([[3, 3], [1, 4], [1, 1], [2, 1], [2, 2]], 3),
        ([[0, 0], [4, 5], [7, 8], [8, 9], [5, 6], [3, 4], [1, 1]], 5)
    ]
    for case in cases:
        res = s.maxPoints(*case[:-1])
        print(res, case[-1])
