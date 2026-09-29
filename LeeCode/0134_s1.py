class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        贪心算法：
            如果总油量小于总花费，则肯定不能跑完一圈
            否则可以通过每个站点的油耗差来遍历一（相较于简单解法判断只需要扫一遍）
                gas: 5 8 2 8
                cost: 6 5 6 6
                dif: -1 3 -4 2
                遍历 dif 可知当当前油箱 < 0 说明当前起点不可行，
        """
        if sum(gas) < sum(cost):  # O(N)
            return -1
        else:
            start = 0
            tank = 0
            for i in range(len(gas)):
                tank += gas[i] - cost[i]
                if tank < 0:
                    # i 及之前的站点都不可能是起点
                    start = i + 1
                    tank = 0
            return start

    def canCompleteCircuitV1(self, gas: list[int], cost: list[int]) -> int:
        """
        简单解法： 依次判断每个点是否可以出发
            O(N^2) 超时
        """

        def check(start: int) -> bool:
            cur_gas = 0
            pos = start
            cnt = 0  # 记录走了多少个站点，因为直接通过pos来判断会出现矛盾
            while cnt < len(gas):
                cur_gas += gas[pos]
                if cur_gas < cost[pos]:  # 油不够到下一站
                    return False
                cur_gas -= cost[pos]
                pos = (pos + 1) % len(gas)
                cnt += 1
            return True

        for i in range(len(gas)):
            if check(i):
                return i

        return -1


if __name__ == '__main__':
    cases = [
        (
            ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
            3
        ),
        (
            ([2, 3, 4], [3, 4, 3]),
            -1
        ),
        (
            ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]),
            4
        ),
        (
            ([5, 8, 2, 8], [6, 5, 6, 6]),
            3
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.canCompleteCircuit(*case[0])
        print(res, case[1])
