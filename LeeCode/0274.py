class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        桶记数法： 因为 H 指数不能超过数组长度n,所以可以引入一个额外的记数数组，
            这个数组第 i 个位置来记录引用数为 i 的论文数量，特别的第 n 个位置代表大于等于n的引用次数的论文数量
        """
        counter = [0] * (len(citations) + 1)
        n = len(citations)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1

        # 累加
        total = 0
        i = len(counter) - 1
        while i >= 0:
            total += counter[i]
            if total >= i:
                return i
            i -= 1
        return 0

    def hIndexV3(self, citations: list[int]) -> int:
        """
        二分搜索法，因为 h 指数肯定在 0~n 之间，可以通过二分搜索，利用 logN 次搜索，每次判断一下是否正确
        得到 O(N * logN) 的复杂度
        """
        left, right = 0, len(citations)
        h = 0
        while left <= right:
            mid = (left + right) // 2
            cnt = 0  # 记录符合条件的论文数量
            for c in citations:
                if c >= mid:
                    cnt += 1
            if cnt >= mid:
                h = mid
                left = mid + 1
            else:
                right = mid - 1
        return h

    def hIndexV2(self, citations: list[int]) -> int:
        """
        简单直观的解法： 先降序排列，然后依次检测
        """
        citations.sort(reverse=True)  # O(N * logN)
        h = 0
        for i, c in enumerate(citations, start=1):
            if c >= i:
                h = i
            else:
                break
        return h

    def hIndexV1(self, citations: list[int]) -> int:
        """
        简单直观的解法： 先降序排列，然后依次检测即可
        时间复杂度 O(N * logN)， 空间复杂度 O(1)
        """
        n = len(citations)
        citations.sort(reverse=True)  # O(N * logN)
        for i in reversed(range(1, n + 1)):  # 从 n 到 1 尝试是否正确  O(N)
            if citations[i - 1] >= i:
                return i
        return 0


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3, 0, 6, 1, 5], 3),
        ([99, 0, 98, 1, 100], 3),
        ([1, 3, 1], 1),
        ([1], 1),
        ([100], 1),
    ]
    for case in cases:
        r = solution.hIndexV3(case[0])
        print(r, case[1])
