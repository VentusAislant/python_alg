import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    cases = [
        (
            [3, 2, 1, 5, 6, 4], 2, 5
        ),
        (
            [3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.findKthLargest(*case[:-1])
        print(res, case[-1])
