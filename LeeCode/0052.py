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

    def totalNQueens(self, n: int) -> int:
        """
        皇后可以攻击同一行或同一列或同一斜线上的棋子，
        n 个皇后如何放置在 n*n 的棋盘上，使得皇后之间不能相互攻击
        """
        cols = []  # 每一行一个皇后，记录每行的皇后列位置即可
        self.res = 0

        def backtrack():
            if len(cols) == n:
                # n 个皇后都已就位
                self.res += 1
                return

            for col in range(n):
                if self.checkValid(cols, col):  # 只会搜索符合条件的位置，减枝一大部分
                    cols.append(col)
                    backtrack()
                    cols.pop()

        backtrack()
        return self.res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            4,
            2
        ),
        (
            1,
            1
        )
    ]
    for case in cases:
        res = solution.totalNQueens(*case[:-1])
        print(res, case[-1])
