class TrieNode:
    def __init__(self, val: str, is_word: bool = False):
        self.val = val
        self.is_word = is_word
        self.children = {}  # str: TrieNode 方便快速获得孩子结点


class WordDictionary:
    """
    词典类 WordDictionary, 支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配
    可以使用前缀树的结构，但是 search 函数需要特别处理，因为可能出现 . 代表任意字符
    """

    def __init__(self):
        self.root = TrieNode('')

    def addWord(self, word: str) -> None:
        """
        向前缀树中插入字符串 word
        """
        cur_node = self.root
        for idx, char in enumerate(word):
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode(char)
            cur_node = cur_node.children[char]
            if idx == len(word) - 1:
                cur_node.is_word = True

    def search(self, word: str) -> bool:
        """
        单词中出现 . 需要判断所有孩子子树中是否有符合条件的单词，因此需要回溯
        可以使用递归算法
        """

        def dfs(node: TrieNode, idx: int) -> bool:
            if idx == len(word):  # root 占用了 idx = 0 的位置，因此这里没问题
                # 走到了单词末尾
                return node.is_word

            char = word[idx]
            # 普通字符
            if char != '.':
                if char not in node.children:
                    return False
                return dfs(node.children[char], idx + 1)
            else:
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
                return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    cases = [
        (
            ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
            [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
            [None, None, None, None, False, True, True, True]
        )
    ]
    for case in cases:
        wd = None
        res = []
        for op, args in zip(*case[:-1]):
            if op == 'WordDictionary':
                wd = WordDictionary()
                res.append(None)
            elif op == 'addWord':
                wd.addWord(*args)
                res.append(None)
            elif op == 'search':
                res.append(wd.search(*args))
        print(res, case[-1])
