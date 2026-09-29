import heapq


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        """
        遍历所有组合，遍历过程中建堆即可， 这种方法会超时
        如何利用有序性，首先可以知道 nums1[0] + nums2[0] 必然是最小的
        假设其中一个坐标固定则
            nums1[i] + nums2[0] < nums1[i] + nums2[1] < ...

        我们首先将所有的 (nums[i], nums2[0]) 压入堆，然后动态将 (nums[i], nums[j]) j>0压入即可判断
        """
        if not nums1 or not nums2 or k==0:
            return []
        heap = []
        res = []

        # 初始化，先压入可能的 k 个最小和即 nums1[:k+1] 分别与 nums2[0] 的和
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        # 动态获取和最小的 k 个对
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if j < len(nums2) - 1:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))

        return res

    def kSmallestPairsV1(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        """
        遍历所有组合，遍历过程中建堆即可， 这种方法会超时
        时间复杂度 O(m*n*log(mn))
        """
        heap = []
        for x in nums1:
            for y in nums2:
                heapq.heappush(heap, (x + y, [x, y]))
        return [item[1] for item in heapq.nsmallest(k, heap)]


if __name__ == '__main__':
    cases = [
        (
            [1, 7, 11], [2, 4, 6], 3,
            [[1, 2], [1, 4], [1, 6]]
        ),
        (
            [1, 1, 2], [1, 2, 3], 2,
            [[1, 1], [1, 1]]
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.kSmallestPairs(*case[:-1])
        print(res, case[-1])
