import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        先考虑 0 来自哪里假设计算 15! = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15
        可以看出 0 来自 5, 10, 15  因为5和15只需要乘个偶数及可以产生0
        因为 10 = 5 * 2, 15 = 5 * 3, 25 = 5 * 5
        25包含两个5， 25*4 = 100 可以产生两个 0，也就是阶乘中包含多少个5的因子
        每个5的因子必然会有一个偶数配对产生一个0
        n // 5 表示找出 n中包含的所有 5 的倍数
        n // 25 表示找出 n 中包含的所有 25 的倍数, 25会多提供一个0
        n // 125 表示找出 n 中包含的所有 125的倍数， 125会比25多提供一个0
        以此类推
        """
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res

    def trailingZeroesv1(self, n: int) -> int:
        """
        简单解法，先计算阶乘，再计算0的数量
        时间复杂度 O(NlogN)
        """
        num = math.factorial(n)  # O(N logN)
        cnt = 0
        while num > 0:
            last_digit = num % 10
            if last_digit == 0:
                cnt += 1
            else:
                break
            num //= 10
        return cnt


if __name__ == '__main__':
    s = Solution()
    cases = [
        (3, 0),
        (5, 1),
        (0, 0),
        (125, 31)
    ]
    for case in cases:
        res = s.trailingZeroes(*case[:-1])
        print(res, case[-1])
