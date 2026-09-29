class Solution:
    def decodeString(self, s: str) -> str:
        """
        数字代表一种重复操作，[xx] 代表字符串 xx
        ab2[a2[bc]] -> ab2[abcbc] -> ababcbcabcbc
        [a, b, 2, '[', a, 2, '[', b, c] 碰到右括号，需要出栈到上一个数字
        [a, b, 2, '[', a, 'bcbc'] 继续入栈又碰到右括号，出栈到上一个数字
        [a, b, 2, 'abcbc'] -> [a, b, 'abcbcabcbc']
        用一个栈即可
            遇到数字，解析多个连续的数字位，入栈
            遇到字符入栈，左括号可以不入栈，因为用数字也可以判断上一层嵌套位置
            遇到右括号开始出栈，一直出栈到上一个数字，需要把结果压入栈顶
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stack.append(num)
            elif s[i].isalpha():
                stack.append(s[i])
                i += 1
            elif s[i] == '[':
                i += 1
            elif s[i] == ']':
                # 出栈到上一个数字
                pop_e = stack.pop()
                ss = ""
                while not isinstance(pop_e, int):
                    ss = pop_e + ss
                    pop_e = stack.pop()
                ss = ss * pop_e
                stack.append(ss)
                i += 1

        res = ''
        for ss in stack:
            res += ss
        return res


if __name__ == '__main__':
    cases = [
        ('3[a]2[bc]', "aaabcbc"),
        ('3[a2[c]]', "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
        ("3[z]2[2[y]pq4[2[jk]e1[f]]]ef", "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")
    ]
    solution = Solution()
    for case in cases:
        res = solution.decodeString(*case[:-1])
        print(res, case[-1])
