class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        python 中 int() 类型转换，可以指定原格式的进制
            int(s, 2)： 将二进制字符串 s 转化为 int 类型
            bin(): 可以转化为二进制字符串
        """
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    cases = [
        (
            "11", "1",
            "100"
        ),
        (
            "1010", "1011",
            "10101"
        ),
    ]
    solution = Solution()
    for case in cases:
        res = solution.addBinary(*case[:-1])
        print(res, case[-1])
