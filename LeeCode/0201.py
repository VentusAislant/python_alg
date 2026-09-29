class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        关键是找到最前面的全部为1的部分，因为只要某个数的某个位位0，结果对应位置就是0
        这个部分可以通过 left 和 right 的公共前缀找到
        可以通过对 right 不断消尾部的 1 ，直到 和 left 相同即可得到这个公共前缀
        """
        while right > left:
            right &= right - 1
        return right

    def rangeBitwiseAndV2(self, left: int, right: int) -> int:
        """
        先看一个例子 [26, 30]
        26  11010
        27  11011
        28  11100
        29  11101
        30  11110
        结果 -> 11010 -> 11000 -> 11000 -> 11000
        关键是找到最前面的全部为1的部分，因为只要某个数的某个位位0，结果对应位置就是0
        这个部分可以通过 left 和 right 的公共前缀找到
        """
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

    def rangeBitwiseAndV1(self, left: int, right: int) -> int:
        """
        时间复杂度过高，计算 [1, 2147483647], 明显会超时
        O(N)
        """
        res = left
        for i in range(left + 1, right + 1):
            res &= i
        return res


if __name__ == '__main__':
    cases = [
        (
            [5, 7],
            4
        ),
        (
            [0, 0],
            0
        ),
        (
            [1, 2147483647],
            0
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.rangeBitwiseAnd(*case[0])
        print(res, case[-1])
