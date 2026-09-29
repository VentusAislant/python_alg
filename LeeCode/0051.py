class Solution:
    def checkValid(self, pos: list[int], new_col: int) -> bool:
        """
        判断插入当前 new_pos 是否合法
        """
        row = len(pos)
        for r, c in enumerate(pos):
            if c == new_col:  # 列冲突
                return False
            if abs(r - row) == abs(c - new_col):  # 对角线冲突
                return False
        return True

    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        皇后可以攻击同一行或同一列或同一斜线上的棋子，
        n 个皇后如何放置在 n*n 的棋盘上，使得皇后之间不能相互攻击
        """
        res = []
        cols = []  # 每一行一个皇后，记录每行的皇后列位置即可

        def backtrack():
            if len(cols) == n:
                # n 个皇后都已就位
                # board = [["."] * n] * n  # !!!这个写法是错误的，因为 * 会使得所有的这一行引用同一个列表对象
                board = [["."] * n for _ in range(n)]
                for row, col in enumerate(cols):
                    board[row][col] = 'Q'
                res.append([''.join(row) for row in board])
                return

            for col in range(n):
                if self.checkValid(cols, col):  # 只会搜索符合条件的位置，减枝一大部分
                    cols.append(col)
                    backtrack()
                    cols.pop()

        backtrack()
        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            4,
            [
                [".Q..", "...Q", "Q...", "..Q."],
                ["..Q.", "Q...", "...Q", ".Q.."]
            ]
        ),
        (
            1,
            [["Q"]]
        )
    ]
    for case in cases:
        res = solution.solveNQueens(*case[:-1])
        print(res, case[-1])
