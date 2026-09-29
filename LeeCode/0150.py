class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        后缀表达式求值 较 中缀转后缀 更为简单
        只需要顺序读取字符串，如果是操作数则入栈，如果是运算符 (+, -, *, /) 则 pop 栈顶两个元素执行运算后压回栈顶即可
        最后栈顶元素即为表达式的值
        """
        stack = []
        operators = ('+', '-', '*', '/')
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                else:
                    res = int(a / b)
                stack.append(res)

        return stack[-1] if stack else 0


if __name__ == '__main__':
    cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ]
    solution = Solution()
    for case in cases:
        res = solution.evalRPN(*case[:-1])
        print(res, case[-1])
