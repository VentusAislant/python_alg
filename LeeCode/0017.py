from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        递归回溯版本
        """
        digit2str = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        res = []

        def backtrack(idx, path):
            """
            需要 idx 才知道当前走了多少层，本质上这个还是多层循环
            """
            if len(path) == len(digits):
                res.append(''.join(path))
                return

            for char in digit2str[int(digits[idx])]:
                path.append(char)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])
        return res

    def letterCombinationsV1(self, digits: str) -> list[str]:
        """
        当前的字母组合源自上一部的字母组合和当前可用字母的组合，可以使用队列先进先出的性质
        例如 digits="234" 需要根据 digits = "23" 时的组合 [ad, bd, cd, ae, be, ce, af, bf, cf] 来构建：
            [ad, bd, cd, ae, be, ce, af, bf, cf] + g
            [ad, bd, cd, ae, be, ce, af, bf, cf] + h
            [ad, bd, cd, ae, be, ce, af, bf, cf] + i
        """
        digit2str = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }

        cur_combination_queue = deque()

        for digit in digits:
            if len(cur_combination_queue) == 0:
                for char in digit2str[int(digit)]:
                    cur_combination_queue.append(char)
            else:
                for _ in range(len(cur_combination_queue)):
                    cur_start = cur_combination_queue.popleft()
                    for char in digit2str[int(digit)]:
                        cur_combination_queue.append(cur_start + char)

        return list(cur_combination_queue)


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            "23",
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        ),
        (
            "2",
            ["a", "b", "c"]
        )
    ]
    for case in cases:
        res = solution.letterCombinations(*case[:-1])
        print(res, case[-1])
