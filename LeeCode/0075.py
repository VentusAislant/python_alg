from collections import defaultdict


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        也可以用一个指针来交换0， 一个指针来交换 2
            p0 = 0, p2 = len(nums) - 1
            p0 向右移动， p2向左移动，当 i 超过 p2 即可停止
        从左往右遍历过程中
            nums[i] == 0, 则 swap(nums[i], nums[p0]), p0+=1, i+=1
            nums[i] == 2, 则 swap(nums[i], nums[p2]), p2-=1， i+=1 这么做是不对的
                例如 [2, 0, 1, 2] 遍历第一个元素时 => [2, 0, 1, 2] 但是 i+=1 了直接忽略了开始的 2
                因此这里不能 i+=1， 要一直比较
        """
        p0, p2 = 0, len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1

    def sortColorsV3(self, nums: list[int]) -> None:
        """
        V2的方法中使用了两次遍历，能不能一次遍历完成？我们可以引入一个额外的指针，分别用来交换 0 和 1
        用 p0 来交换 0， 用 p1 来交换 1， 初始值都为 0， 从左向右遍历整个数组
            如果找到 1，使其和 nums[p1] 交换， 并将 p1 后移
            如果找到 0，将其和 nums[p0] 交换，并将 p0 后移，这样可以吗？
                因为连续的 0 后是连续的 1，因此我们交换 0 到前面时 p1 指针需要同步后移
                如果 p0 = p1 说明 此时我们没有将 1 交换到前面，前面都是 0
                    此时我们只需要交换 nums[p0] 和  nums[i]， 然后 p0 和 p1 后移即可
                如果 p0 < p1, 说明我们已经将一些连续的 1 放到了头部
                    我们交换 nums[p0] 和 nums[i] 会将 1 换出去
                    需要再将 1 回到 p1 的位置
        """
        p0, p1 = 0, 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:  # 有 1 被交换到后面
                    nums[p1], nums[i] = nums[i], nums[p1]
                p0 += 1
                p1 += 1
            elif nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            i += 1

    def sortColorsV2(self, nums: list[int]) -> None:
        """
        使用单指针，两次遍历
            第一次遍历，用指针 p 划分区间，p 前面的元素都为 0
            第二次遍历，从上次的 p 开始，继续让 p 前面的元素都为 1即可
        """
        p = 0
        i = 0
        # 第一次遍历
        while i < len(nums):
            if nums[i] == 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
            i += 1

        # 第二次遍历
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
            i += 1

    def sortColorsV1(self, nums: list[int]) -> None:
        """
        最简单的思路，利用一个哈希表 + 两趟扫描
        """
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1

        i = 0
        for j in range(3):
            k = 0
            while k < cnt[j]:
                nums[i] = j
                i += 1
                k += 1


if __name__ == '__main__':
    cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2])
    ]
    solution = Solution()
    for case in cases:
        solution.sortColors(case[0])
        res = case[0]
        print(res, case[-1])
