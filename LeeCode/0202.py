class Solution:
    def isHappy(self, n: int) -> bool:

        """
        快慢指针法，使用哈希表存储可能会浪费很多存储空间，如何设计 O(1) 空间复杂度的算法
        算法关键部分就是判断循环，前者判断循环使用一个哈希表进行记录，但是能否不用额外空间判断循环呢
        可以采用快慢指针，慢指针一次走一步，快指针一次走两步，
            如果没有循环，则快指针会比慢指针先到达数字1
            如果有循环，那么快慢指针会在同一个数字相遇
        """

        def get_next(number):
            new_n = 0
            while number > 0:
                new_n += (number % 10) ** 2
                number //= 10
            return new_n

        slow, fast = n, get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1

    def isHappyV1(self, n: int) -> bool:
        """
        因为重复将该数替换为每个位置上的数字的平方和，可能出现两种情况
            无限循环始终边不到 1
            重复这个过程直到 1
        所以可以用一个 set 记录出现过的元素，如果重复出现，说明陷入循环
        """
        seen = set()
        while n != 1:
            seen.add(n)

            new_n = 0
            while n > 0:
                new_n += (n % 10) ** 2
                n = n // 10

            n = new_n
            if n in seen:
                break

        if n != 1:
            return False
        else:
            return True


if __name__ == '__main__':
    cases = [
        (19, True),
        (2, False),
    ]
    solution = Solution()
    for case in cases:
        res = solution.isHappy(case[0])
        print(res, case[1])
