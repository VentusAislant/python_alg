class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        问题本质：对于第 i 天，找到右侧第一个比 temperatures[i] 高的第 j 天， 输出 j-i
        我们需要有一个单调递减栈 （从栈底到栈顶温度递减）来存放截止目前的没有确定的天的索引
        每到一天，既可以检查一遍单调栈，从顶到底弹出所有温度小于当前天的索引，因为他们已经可以确定了就是 i-prev

        [73, 74, 75, 71, 69, 72, 76, 73]
            i=0, push 0 -> [0]
            i=1, 74>73, pop 0 -> []  res = [1-0] = [1]
                 push 1 -> [1]
            i=2, 75>74, pop 1 -> []  res = [1, 2-1] = [1, 1]
                 push 2 -> [2]
            i=3, 71<74, push 3 -> [2, 3]
            i=4, 69<71, push 4 -> [2, 3, 4]
            i=5, 72>69, pop 4 -> [2, 3] res = [1, 1, x, x, 5-4] = [1, 1, x, x, 1]
                 72>71, pop 3 -> [2] res = [1, 1, x, 5-3, 1] = [1, 1, x, 2, 1]
                 72<75, push 5 -> [2, 5]
            i=6, 76>72, pop 5 -> [2] res = [1, 1, x, 2, 1, 6-5] = [1, 1, x, 2, 1, 1]
                 76>75, pop 2 -> []  res = [1, 1, 6-2, 2, 1, 1] = [1, 1, 4, 2, 1, 1]
                 push 6 -> [6]
            i=7, 73<76, push 7 -> [6, 7]
                => res =  [1, 1, 4, 2, 1, 1, 0, 0]
        """
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n):
            # 当前温度比栈顶高，说明找到了答案
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res


if __name__ == '__main__':
    cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
    ]
    solution = Solution()
    for case in cases:
        res = solution.dailyTemperatures(*case[:-1])
        print(res, case[-1])
