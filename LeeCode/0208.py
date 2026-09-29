class TrieNode:
    def __init__(self, val: str, is_word: bool = False):
        self.val = val
        self.is_word = is_word
        self.children = {}  # str: TrieNode 方便快速获得孩子结点


class Trie:
    """
    Trie (前缀树) 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
    这一数据结构有相当多的应用情景，例如自动补全和拼写检查。
    假设有三个单词 app, apple, apart 则可以构建如下 Trie
                   ' '
                    |
                    a
                    |
                    p
                   / \
                  p*  a
                 |     \
                 l      r
                |       \
               e*        t*
    """

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
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
        如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）
        否则，返回 false
        """
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return cur_node.is_word  # 检查当前结点是否是完整单词

    def startsWith(self, prefix: str) -> bool:
        """
        如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true
        否则，返回 false
        """
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    cases = [
        (
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True]
        )
    ]
    for case in cases:
        trie = None
        res = []
        for op, args in zip(*case[:-1]):
            if op == 'Trie':
                trie = Trie()
                res.append(None)
            elif op == 'insert':
                trie.insert(*args)
                res.append(None)
            elif op == 'search':
                res.append(trie.search(*args))
            elif op == 'startsWith':
                res.append(trie.startsWith(*args))
        print(res, case[-1])
