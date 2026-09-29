class Solution:
    def align(self, words: list[str], max_width) -> str:
        """
        传入一个单词列表，把单词列表转化为固定 max_width 长度的字符串，
        字符串中的空格需要均匀分配到单词间，如果不能均匀分配则左侧空格多于右侧
        给定的 words 必定满足条件
        """
        num_words = len(words)
        if num_words == 1:
            return words[0] + ' ' * (max_width - len(words[0]))

        total_space = max_width - sum([len(w) for w in words])
        space_lst = [total_space // (num_words - 1)] * (num_words - 1)
        left_space = total_space - (total_space // (num_words - 1) * (num_words - 1))

        i = 0
        while left_space > 0 and i < len(space_lst):
            space_lst[i] += 1
            left_space -= 1
            i += 1

        res = ""
        for i, word in enumerate(words):
            res += word
            if i < len(words) - 1:
                res += ' ' * space_lst[i]

        return res

    def fullJustify(self, words: list[str], max_width: int) -> list[str]:
        cur_len = 0
        cur_row_words = []
        res = []
        for i in range(len(words)):
            cur_len += len(words[i])
            cur_row_words.append(words[i])
            if cur_len + len(cur_row_words) - 1 > max_width:
                # 需要下一行
                cur_row_words.pop()
                res.append(self.align(cur_row_words, max_width))
                cur_len = len(words[i])
                cur_row_words = [words[i]]

        if cur_row_words:
            last = " ".join(cur_row_words)
            last += " " * (max_width - len(last))
            res.append(last)

        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            ["This", "is", "an", "example", "of", "text", "justification."], 16,
            [
                "This    is    an",
                "example  of text",
                "justification.  "
            ]
        ),
        (
            ["What", "must", "be", "acknowledgment", "shall", "be"], 16,
            [
                "What   must   be",
                "acknowledgment  ",
                "shall be        "
            ]
        ),
        (
            ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
             "Art", "is", "everything", "else", "we", "do"], 20,
            [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  "
            ]
        ),
        (
            ["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do",
             "for", "your", "country"], 16,
            ["ask   not   what", "your country can", "do  for  you ask", "what  you can do", "for your country"]
        ),
        (
            ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
             "Art", "is", "everything", "else", "we", "do"],
            20,
            ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is",
             "everything  else  we", "do                  "]
        ),
    ]
    for case in cases:
        result = solution.fullJustify(*case[:-1])
        print(f'{result}\n{case[-1]}')
