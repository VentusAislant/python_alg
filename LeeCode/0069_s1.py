import math


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        使用 exp 和 ln 代替平方根操作
            x^{0.5} = (e^{lnx})^0.5 = e^(0.5lnx)
        由于计算机无法存储浮点数的精确值，计算时候会导致误差最后得到错误结果
        比如计算 x = 2147395600， 得到的结果 46339 和正确答案 46340 相差1，需要额外判断
        """
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x, math.exp(1))))
        return ans + 1 if (ans + 1) * (ans + 1) <= x else ans

    def mySqrtV3(self, x: int) -> int:
        """
        牛顿迭代法
            目标是 找函数 f(y) 的零点 y*, 即 f(y*) = 0
            我们的题目是计算 x^0.5 将最终结果记为 y, 则计算 y = x^0.5 (x为常数，y为未知变量)
            y^2 = x, 即求解 y^2 - x = 0 也就是求 f(y) = y^2 -x = 0 的根

            根据牛顿迭代法
                f(y) = f(y_n) + f'(y_n)(y-y_n) + o(y)
                y_{n+1} = y_n - f(y_n) / f'(y_n)
                代入 f(y) = y^2 - x => f'(y) = 2y
                y_{n+1} = y_n - f(y_n) / f'(y_n) = y_n - (y_n^2 - x) / 2y_n
                        = (y_n + x/y_n) / 2
        """
        if x == 0:
            return 0

        yn = x
        while yn * yn > x:
            yn = (yn + x // yn) // 2
        return yn

    def mySqrtV2(self, x: int) -> int:
        """
        二分查找，因为要求的是整数，可以直接通过二分搜索来找到
        """
        if x < 2:
            return x

        l, r = 1, x // 2
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r

    def mySqrtV1(self, x: int) -> int:
        """
        题目不允许使用内置函数
        """
        return math.floor(math.sqrt(x))


if __name__ == '__main__':
    s = Solution()
    cases = [
        (4, 2),
        (8, 2),  # 小数部分被舍弃
    ]
    for case in cases:
        res = s.mySqrt(*case[:-1])
        print(res, case[-1])
