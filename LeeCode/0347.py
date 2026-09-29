from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        首先统计频率，然后利用堆获得前k个高频数即可
        时间复杂度 O(nlogn)
        空间复杂度 O(n)
        """
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        heap = []
        for num, cnt in freq.items():
            heapq.heappush(heap, (-cnt, num))  # 用负号模拟最大堆

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


if __name__ == '__main__':
    cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2]),
        ([1], 1, [1])
    ]
    solution = Solution()
    for case in cases:
        res = solution.topKFrequent(*case[:-1])
        print(res, case[-1])
