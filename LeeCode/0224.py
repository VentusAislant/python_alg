class Solution:
    def calculate(self, s: str) -> int:
        """
        分三步，
            1. 首先对输入字符串进行标准化，因为会出现一些一元运算符 + - 需要在这个一元运算符前面补0
            2. 输入的字符串表达式都是中缀表达式
            3. 需要转为后缀表达式后再借助栈求值
        """
        return self.compute_postfix(self.infix2postfix(self.normalize(s)))

    def normalize(self, s: str) -> str:
        """
        在一元 + 或 - 前 插入 一个 0
        """
        out = []
        for i, char in enumerate(s):
            if char in '+-':
                # 查找前一个非空字符
                j = i - 1
                while j >= 0 and s[j].isspace():
                    j -= 1

                if j == -1 or s[j] in ['(', '+', '-']:
                    # 前面没有符号，或者前面是 ( + - 说明当前字符是一元运算符
                    out.append('0')

            out.append(char)
        return ''.join(out)

    def infix2postfix(self, s: str) -> list[str | int]:
        """
        无法处理一元运算符 + -
        中缀表达式转后缀表达式，运算符包括 `(` `)` `+` `-`
        遍历中缀表达式的字符
            如果是操作数直接加入到输出列表即可
            如果是运算符，需要借助辅助栈来进行判断
                如果是左括号，则压入栈顶
                如果是右括号，则出栈到上一个左括号，将中间出栈的非括号运算符加入到输出列表
                加号和减号：
                    优先级相同，需要先把栈顶已有的操作的 + 和 - 弹出
        """

        res = []
        stack = []

        i = 0
        while i < len(s):
            char = s[i]
            if char.isspace():
                i += 1
                continue

            elif char.isdigit():
                # 需要处理多位数字的情况
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                res.append(num)
                continue

            elif char == '(':
                stack.append(char)

            elif char == ')':
                while stack and stack[-1] != '(':
                    res.append(stack.pop())
                stack.pop()  # 弹出左括号

            elif char in ['+', '-']:
                # 前面优先级相同的运算符需要出栈
                while stack and stack[-1] in ['+', '-']:
                    res.append(stack.pop())
                stack.append(char)
            i += 1

        while stack:
            res.append(stack.pop())

        return res

    def compute_postfix(self, tokens: list[str | int]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-"]:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
        return stack[-1]


if __name__ == '__main__':
    cases = [
        ("1 + 1", 2),
        ("2-1 + 2", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
        ("1-(     -2)", 3),
        ("- (3 + (4 + 5))", -12)
    ]
    solution = Solution()
    for case in cases:
        res = solution.calculate(case[0])
        print(res, case[1])
