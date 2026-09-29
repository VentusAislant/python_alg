class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        遍历每个格子，计算当前格子周围的存活细胞数量 around_live_count
        因为需要原地算法，所以不能使用额外的空间记录哪些细胞需要修改状态，因为数组取值只有 0 和 1
        可以在对应位置上用
            -1 表示 alive -> dead 即 1 变化到 0
            -2 表示 dead -> alive 即 0 变化到 1
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                # 计算当前格子周围的存活细胞数量
                around_live_count = 0
                l, t = i - 1 if i - 1 >= 0 else 0, j - 1 if j - 1 >= 0 else 0
                r, b = i + 1 if i + 1 < len(board) else i, j + 1 if j + 1 < len(board[i]) else j
                for x in range(l, r + 1):
                    for y in range(t, b + 1):
                        if (x, y) != (i, j):
                            if board[x][y] == 1 or board[x][y] == -1:
                                around_live_count += 1

                # dead -> alive
                if board[i][j] == 0 and around_live_count == 3:
                    board[i][j] = -2  # 直接修改会影响后续算法

                # alive -> dead
                if board[i][j] == 1 and (around_live_count < 2 or around_live_count > 3):
                    board[i][j] = -1

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == -2:
                    board[i][j] = 1


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]),
        ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
        ([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])
    ]
    for case in cases:
        solution.gameOfLife(case[0])
        print(case[0], case[1])
