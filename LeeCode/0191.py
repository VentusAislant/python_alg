class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Brian Kernighan 算法
            n = 1011000
            n-1 = 1010111
            n & (n-1) = 1010000
            可以直接吧最低位的 1 抵消掉
        """
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

    def hammingWeightV1(self, n: int) -> int:
        """
        不断向右移位，遇到1，结果+1即可
        """
        res = 0
        while n > 0:
            res += n & 1
            n >>= 1
        return res


if __name__ == '__main__':
    cases = [
        (
            11,
            3
        ),
        (
            128,
            1
        ),
        (
            2147483645,
            30
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.hammingWeight(*case[:-1])
        print(res, case[-1])
