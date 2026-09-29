class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        回溯所有可能的组合即可
        如何判断当前括号组有效？
            需要实时记录左右括号数量,
                左括号数量 < n 即可插入左括号
                右括号数量 < 左括号数量 即可插入右括号
        """
        res = []
        path = []
        self.left_cnt = 0
        self.right_cnt = 0

        def backtrack():
            if len(path) == 2 * n:
                res.append(''.join(path))
                return

            if self.left_cnt < n:
                # 尝试添加左括号
                path.append('(')
                self.left_cnt += 1
                backtrack()
                path.pop()
                self.left_cnt -= 1

            if self.right_cnt < self.left_cnt:
                path.append(')')
                self.right_cnt += 1
                backtrack()
                path.pop()
                self.right_cnt -= 1

        backtrack()
        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            3,
            ["((()))", "(()())", "(())()", "()(())", "()()()"]
        ),
        (
            1,
            ["()"]
        )
    ]
    for case in cases:
        res = solution.generateParenthesis(*case[:-1])
        print(res, case[-1])
