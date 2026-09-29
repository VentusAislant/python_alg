class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        """
        因为单词长度是一样的，可以讲字符串从不同起点按固定长度分成若干个块，例如
            barfoothefoobarman 可以分为
            bar | foo | the | foo | bar | man
            b | arf | oot | hef | oob | arm | an
            ba | rfo | oth | efo | oba | rma | n

        每个块看作一个元素，使用滑动窗口的方法，找到所有窗口大小为 len(words) 的起点即可
        为了记录窗口中是否出现了全部的 words 中的单词 (可能重复)，需要一个 dict 来记录
        """
        res = []
        word_len = len(words[0])
        num_words = len(words)
        str_len = len(s)
        need = {}
        for w in words:
            if w in need:
                need[w] += 1
            else:
                need[w] = 1

        for offset in range(word_len):
            # [0, word_len-1]
            # 获得当前偏移量下的所有合法块的起点索引
            start_idx_lst = list(i for i in range(offset, str_len, word_len) if i + word_len <= str_len)
            # 获得当前偏移量下所有合法的单词
            word_lst = [s[idx:idx+word_len] for idx in start_idx_lst]

            left = 0
            count = 0 # 记录当前窗口包含多少合法单词
            cur_window = {k:0 for k in need}
            for right in range(len(word_lst)):
                cur_word = word_lst[right]

                if cur_word in need:
                    cur_window[cur_word] += 1
                    count += 1

                    # 如果某个单词数量超过需要，则需要收缩左边界知道符合 need 要求
                    while cur_window[cur_word] > need[cur_word]:
                        left_word = word_lst[left]
                        cur_window[left_word] -= 1
                        left += 1
                        count -= 1

                    # 如果窗口正好包含 num_words 个单词说明找到了一个合法的位置
                    if count == num_words:
                        res.append(offset + left * word_len)
                else:
                    # 当前单词不在 need 中，需要清空窗口
                    cur_window = {k:0 for k in need}
                    count = 0
                    left = right + 1
        return res

    def findSubstringV1(self, s: str, words: list[str]) -> list[int]:
        """
        简单解法，words 列表元素个数为 m, 每个元素的长度为 n，计算所有串联子串 (n!) 种
        遍历 s 中长度为 m*n 的子串

        时间复杂度 O(L * m!) 过高

        Python 内置库 itertools.permutations 可以快捷生成一个列表中元素的全排列

            ```
            import itertools

            nums = [1, 2, 3]
            perms = list(itertools.permutations(nums))

            print(perms)  # [(1, 2, 3), (1, 3, 2), ...]
            ```

        """
        import itertools
        perms = [''.join(ws) for ws in itertools.permutations(words)]
        len_sub_str = len(words) * len(words[0])
        res = []
        for i in range(len(s) - len_sub_str + 1):
            if s[i:i+len_sub_str] in perms:
                res.append(i)
        return res


if __name__ == '__main__':
    cases = [
        ("barfoothefoobarman", ["foo","bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
        ("barfoofoobarthefoobarman", ["bar","foo","the"], [6, 9, 12]),
        ("wordgoodgoodgoodbestword", ["word","good","best","good"], [8])
    ]

    solution = Solution()
    for case in cases:
        my_answer = solution.findSubstring(*case[:-1])
        print(my_answer, case[-1])
