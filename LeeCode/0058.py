class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        从零实现的话：逆序遍历，从第一个非空字符开始记数到下一个非空字符截止
        """
        res = 0
        start = False
        for i in range(len(s)-1, -1, -1):
            if not start:
                if s[i] != ' ':
                    start = True
                    res += 1
            else:
                if s[i] != ' ':
                    res += 1
                else:
                    break
        return res

    def lengthOfLastWordV1(self, s: str) -> int:
        return len(s.split()[-1])


if __name__ == '__main__':
    cases = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6)
    ]
    solution = Solution()
    for case in cases:
        res = solution.lengthOfLastWord(case[0])
        print(res, case[1])
