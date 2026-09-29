class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        可以采用翻转一半数字，然后和另一半数字比较的方法
        时间复杂度 O(logN), 空间复杂度 O(1)
        """
        if x < 0:
            return False
        if x != 0 and x % 10 == 0:
            # 以0结尾的非0数字肯定不是回文数
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10
        return x == reverted or x == reverted // 10  # 奇数情况 reverted 比 x 多 1位

    def isPalindromeV2(self, x: int) -> bool:
        """
        双向指针方法， 但是转化成字符串需要 O(N) 的时间复杂度 空间复杂度 O(N)
        """
        lst = list(str(x))
        i, j = 0, len(lst) - 1
        while i < j:
            if lst[i] != lst[j]:
                return False
            i += 1
            j -= 1
        return True

    def isPalindromeV1(self, x: int) -> bool:
        # 转化成字符串来判断
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    s = Solution()
    cases = [
        (1221, True),
        (12121, True),
        (222111, False),
    ]
    for case in cases:
        res = s.isPalindrome(*case[:-1])
        print(res, case[-1])
