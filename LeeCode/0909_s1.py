from collections import deque


class Solution:
    def num2ij(self, num, n):
        """
        num 表示格子对应的数字
        n 表示棋盘边长
        返回格子的坐标
        """

        # 当前数字在第 n - 1 - tmp 行
        tmp = (num - 1) // n
        row_id = n - 1 - tmp

        x_dir = tmp % 2 == 0  # 如果为 True 则表示向右的
        if x_dir:
            col_id = (num - 1) % n
        else:
            col_id = n - 1 - (num - 1) % n
        return row_id, col_id

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        """
        模拟广度优先遍历即可，当前结点可能的步只有接下来 6 格
        """
        n = len(board)
        start, end = 1, n * n
        queue = deque([(start, 0)])  # (位置, 步数)
        visited = {start}

        while queue:
            pos, step = queue.popleft()
            if pos == end:
                return step

            for i in range(1, 7):
                next_pos = pos + i
                if next_pos > end:
                    break

                x, y = self.num2ij(next_pos, n)
                if board[x][y] != -1:
                    next_pos = board[x][y]

                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, step + 1))

        return -1


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1]
            ],
            4
        ),
        (
            [
                [-1, -1],
                [-1, 3]
            ],
            1
        ),
    ]
    for case in cases:
        res = solution.snakesAndLadders(*case[:-1])
        print(res, case[-1])
