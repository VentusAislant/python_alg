import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        """
        总共可以进行 k 轮项目投资，w 为当前的资金，每次选择可以启动的项目中，收益最高那个即可
        可以通过构建一个堆，动态将当前可进行的项目 push 到堆中，因为当前资金肯定会大于上一轮可调度资金
        """
        cur_w = w
        heap = []
        i = 0  # 已经用过的项目

        profits, capital = zip(*sorted(zip(profits, capital),  key=lambda x: x[1]))

        for _ in range(k):
            while i < len(capital):
                p, c = profits[i], capital[i]
                if cur_w < c:
                    break
                else:
                    heapq.heappush(heap, -p)  # 默认用第一个元素构建最小堆，因此取负
                    i += 1

            if not heap:
                break

            cur_max_profit = - heapq.heappop(heap)
            cur_w += cur_max_profit
        return cur_w


if __name__ == '__main__':
    cases = [
        (
            2, 0, [1, 2, 3], [0, 1, 1], 4
        ),
        (
            3, 0, [1, 2, 3], [0, 1, 2], 6
        ),
        (
            1, 0, [1, 2, 3], [1, 1, 2], 0
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.findMaximizedCapital(*case[:-1])
        print(res, case[-1])
