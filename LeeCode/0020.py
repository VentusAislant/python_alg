class Solution:
    def isValid(self, s: str) -> bool:
        """
        括号匹配，遇左括号入栈，遇右括号根据匹配情况尝试出栈
        """
        stack = []
        map = {')': "(", "]": "[", "}": "{"}
        for char in s:
            if stack and char in map:
                # 右括号，尝试出栈
                if stack[-1] != map[char]:
                    # 不匹配
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0


if __name__ == '__main__':
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True)
    ]
    solution = Solution()
    for s, a in cases:
        my_answer = solution.isValid(s)
        print(my_answer, a)
