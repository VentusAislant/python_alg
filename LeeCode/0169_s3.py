import random
from typing import List, Optional
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int], choice='voting') -> Optional[int]:
        if choice == 'voting':
            return self.votingMajorityElement(nums)
        elif choice == 'random':
            return self.randomMajorityElement(nums)
        elif choice == 'hash':
            return self.hashMajorityElement(nums)
        elif choice == 'sort':
            return self.sortMajorityElement(nums)
        else:
            raise NotImplementedError

    def votingMajorityElement(self, nums: List[int]) -> Optional[int]:
        # 投票算法
        votes = 0
        candidate = None
        for num in nums:
            if votes == 0:
                candidate = num
            if num == candidate:
                votes += 1
            else:
                votes -= 1
        return candidate

    def randomMajorityElement(self, nums: List[int]) -> Optional[int]:
        """
        # 随机算法
            期望时间复杂度为 O(N), 主要来自检测这个数是不是众数, 空间复杂度为 O(1)
            随机选到众数的期望次数是 2，即常数复杂度
        """
        def is_right(candidate):
            cnt = 0
            for num in nums:
                if num == candidate:
                    cnt += 1
            return cnt > len(nums) // 2

        unvisited = list(range(len(nums)))
        while len(unvisited) > 0:
            choice = random.choice(unvisited)
            unvisited.remove(choice)
            if is_right(nums[choice]):
                return nums[choice]
        return None

    def hashMajorityElement(self, nums: List[int]) -> Optional[int]:
        """
        # 哈希表算法
        """
        counter = Counter(nums)
        for k, v in counter.items():
            if v > len(nums) // 2:
                return k
        return None

    def sortMajorityElement(self, nums: List[int]) -> Optional[int]:
        """
        对于有序的数组，下表 n/2 处必为众数
            时间复杂度: O(N*logN)
            空间复杂度: O(logN) # 语言自带的排序算法需要额外的栈空间，自己编写堆排序可以为 O(1)
        """
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2)
    ]
    for case in cases:
        for choice in ['random', 'hash', 'sort', 'voting']:
            result = solution.majorityElement(*case[:-1])
            print(result, case[-1])
