class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        先将所有合法的路径元素提取出来，然后依次入栈，当碰到 . 或 .. 等进行出栈
        最后把栈内元素重新用 '/' 拼接，但是需要注意栈为空的情况，
        """
        path_lst = path.split('/')
        stack = []
        for item in path_lst:
            item = item.strip()
            if item == "":
                # 特殊情况
                continue
            elif item in [".", ".."]:
                # 需要出栈 len(item) - 1 次
                i = 0
                while i < len(item) - 1 and stack:
                    stack.pop()
                    i += 1
            else:
                stack.append(item)

        if not stack:
            return "/"
        else:
            return "/" + "/".join(stack)


if __name__ == '__main__':
    cases = [
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/"),
        ("/.../a/../b/c/../d/./", "/.../b/d")
    ]
    solution = Solution()
    for case in cases:
        res = solution.simplifyPath(*case[:-1])
        print(res, case[-1])
