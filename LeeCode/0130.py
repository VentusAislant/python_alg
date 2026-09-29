from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        广度优先遍历，从边界出发找到所有邻近边界的 `O` 的联通区域，然后将这些联通区域之外的 O 变成 X
        """
        m = len(board)
        n = len(board[0])

        queue = deque()

        # 1. 边界上的 O 入队
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    queue.append((i, j))

        for j in range(n):
            for i in [0, m - 1]:
                if board[i][j] == 'O':
                    queue.append((i, j))

        # 2. 利用 BFS 标记所有与边界联通的 O 区域
        while queue:
            x, y = queue.popleft()
            if board[x][y] != 'O':
                continue

            board[x][y] = '*'  # *所在区域为边界的 O 联通区域，之后无需改动

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    # 边界联通的地方
                    queue.append((nx, ny))

        # * 的区域变为 O, O 的区域变为 X
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'X']
            ],
            [
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'X', 'X']
            ]
        ),
        (
            [['X']],
            [['X']]
        ),
        (
            [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"], ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"], ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
             ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"], ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
             ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"], ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
             ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"], ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]],
            [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"], ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X", "X", "O"],
             ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
             ["O", "X", "X", "X", "X", "X", "X", "X", "X", "O"], ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "X", "X", "X", "X", "O", "O"], ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]
        )
    ]
    for case in cases:
        res = solution.solve(*case[:-1])
        print(case[0] == case[-1])
        print(case[0])
        print(case[-1])
