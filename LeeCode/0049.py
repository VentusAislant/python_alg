from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        可以对每个字符串排序，然后将排序后的字符串作为 key,统计这个key下的所有字符串即可
        """
        result = defaultdict(list)
        for s in strs:
            sort_s = ''.join(sorted(s))
            result[sort_s].append(s)
        return [v for k, v in result.items()]

    def groupAnagramsV1(self, strs: list[str]) -> list[list[str]]:
        """
        每个字符串可以对应一个词频表，词频表一样的字符串即为字母异位词，需要分在一个组
        可以先计算每个字符串的词频表，然后按照词频表进行分组，
            result 用来存储每个词频表对应的字符串列表
            因为 Python 中不能使用 dict, list, set 当作 dict 的键，所以需要将词频表排序后转化成 tuple
        """
        result = defaultdict(list)
        for s in strs:
            k = tuple(sorted(Counter(s).items()))
            result[k].append(s)
        return [v for k, v in result.items()]

    def groupAnagramsV2(self, strs: list[str]) -> list[list[str]]:
        """
        字母异位词的核心逻辑是两个字符串的词频一致，所以将词频作为 key, 构建哈希表即可
        把词频相同的字符串放在同一个key下的列表
        需要注意的是字典无法进行哈希，需要将词频转化为有序的tuple,每个元素是一个kv对即可
        """
        res = defaultdict(list)
        for s in strs:
            # 词频表构建
            freq = defaultdict(int)
            for c in s:
                freq[c] += 1
            # 转成 tuple 方便哈希映射
            key = tuple(sorted(freq.items()))
            res[key].append(s)
        return list(res.values())


if __name__ == '__main__':
    cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]])
    ]
    solution = Solution()
    for case in cases:
        res = solution.groupAnagrams(case[0])
        print(case[1], res)
