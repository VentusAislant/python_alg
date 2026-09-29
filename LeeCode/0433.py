from collections import deque, defaultdict


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """
        同 0909 基因序列解法类似，但是如何优化性能，因为 wordList 可能很大，每次 寻找当前单词可能的下一个变化
        会花费很多时间，
        可以构建一个模式字典如
            dog -> *og, d*g, do*
            dot -> *ot, d*t, do*
        两个都属于 do*
            *og = [dog]
            d*g = [dog]
            do* = [dog, dot]
            *ot= [dot]
            d*t = [dot]
        """
        if beginWord == endWord or endWord not in wordList:
            return 0

        # 构建通用模式字典
        pattern_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                cur_pattern = word[:i] + '*' + word[i+1:]
                pattern_dict[cur_pattern].append(word)

       # 使用 BFS
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            cur_word, step = queue.popleft()
            if cur_word == endWord:
                return step
            for i in range(len(cur_word)):
                pattern = cur_word[:i] + '*' + cur_word[i+1:]
                neighbors = pattern_dict[pattern]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, step + 1))

        return 0


if __name__ == '__main__':
    sol = Solution()
    cases = [
        (
            "hit", "cog", ["hot","dot","dog","lot","log","cog"],
            5
        ),
        (
            "hit", "cog", ["hig","cig","cog"],
            4
        ),
        (
            "hit", "cog", ["hot","dot","dog","lot","log"],
            0
        ),
    ]
    for case in cases:
        res = sol.ladderLength(*case[:-1])
        print(res, case[-1])
