class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        二分思想，设 len(nums1) = m, len(nums2) = n
        合并后的左半部分元素个数应为 (m + n + 1) // 2
        在 nums1 中选取切分点 i，则 nums2 中的切分点 j 被唯一确定：
            i + j = (m + n + 1) // 2

        当满足：
            nums1[i-1] <= nums2[j]
            nums2[j-1] <= nums1[i]
        时，切分合法，中位数即可由边界元素得到
        """

        # 确保 i 处在短数组，防止 j 越界
        # i \in [0, m], j \in [0, n] 不会
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        l, r = 0, m
        while l <= r:
            i = (l + r) >> 1
            j = (m + n + 1) // 2 - i

            left1 = float('-inf') if i == 0 else nums1[i - 1]  # nums1 中左半部分最后一个元素
            right1 = float('inf') if i == m else nums1[i]  # nums1 中右半部分第一个元素

            left2 = float('-inf') if j == 0 else nums2[j - 1]
            right2 = float('inf') if j == n else nums2[j]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1

        return -1

    def findMedianSortedArraysV1(self, nums1: list[int], nums2: list[int]) -> float:
        """
        最简单的思路是 merge 两个数组，然后中位数就很好求，但是时间复杂度 O(m+n)
        不符合题目要求的 O(log(m+n))
        """
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        lst = []
        k = 0
        target_pos = (m + n) // 2
        need_pre = (m + n) % 2 == 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                lst.append(nums1[i])
                i += 1
                k += 1
            else:
                lst.append(nums2[j])
                j += 1
                k += 1

        while i < m:
            lst.append(nums1[i])
            i += 1

        while j < n:
            lst.append(nums2[j])
            j += 1

        if need_pre:
            return (lst[target_pos - 1] + lst[target_pos]) / 2.0

        return float(lst[target_pos])


if __name__ == '__main__':
    cases = [
        (
            [1, 3], [2],
            2.0
        ),
        (
            [1, 2], [3, 4],
            2.5
        ),
        (
            [2, 2, 4, 4], [2, 2, 2, 4, 4],
            2.0
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.findMedianSortedArrays(*case[:-1])
        print(res, case[-1])
