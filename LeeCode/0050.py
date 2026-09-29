import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        快速求幂 O(logN)
            当 n 为偶数时，x^n = (x^{n//2})^2
            当 n 为奇数时，x^n = x * x^{n-1}
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        else:
            return x * self.myPow(x, n - 1)

    def myPowV2(self, x: float, n: int) -> float:
        """
        时间复杂度为 O(N)， 过高
        """
        is_minus = n < 0

        if n == 0:
            return 1

        if n < 0:
            n = -n

        res = 1
        for _ in range(n):
            res *= x

        return res if not is_minus else 1 / res

    def myPowV1(self, x: float, n: int) -> float:
        """
        不能直接调用函数
        """
        return math.pow(x, n)


if __name__ == '__main__':
    s = Solution()
    cases = [
        (2.0, 10, 1024.0),
        (2.1, 3, 9.261),
        (2.0, -2, 0.25)
    ]
    for case in cases:
        res = s.myPow(*case[:-1])
        print(res, case[-1])
