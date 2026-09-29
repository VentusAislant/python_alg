from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_height(self, root):
        if root is None:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1

    def exist(self, root: TreeNode, h: int, idx: int) -> bool:
        """
        判断完全二叉树中最后一层的相对索引 idx 是否存在
            h: 表示树高，根为 第 1 层
            idx: 相对编号范围, 取值 [0, 2^(h-1)-1]
        """
        node = root

        """
        假设树高为4，最后一层有 2^(h-1) = 8 个位置，idx 范围是 [0,7]
        对应八个二进制数 [000, 001, 010, 011, 100, 101, 110, 111]
        二进制正好代表这个结点的位置，0 表示选择 left，1 表示选择 right
        因此给定一个特定的 idx,即告诉了其如何层序遍历，按照这个方式遍历查看结点是否为 None即可
        """
        for depth in range(h - 1):
            # 假设 idx = 6 = (110)_2, h-2-depth = 2
            # 则 idx >> 2 = 001 向右移动两位，也就是把原来的二进制的第2位放到各位
            # (idx >> 2) & 1 = (idx >> 2) & 001 只保留个位上的值 0 / 1
            # h - 2 - depth 的迭代顺序为 [h-2, h-3, ..., 0]
            # 也就是从idx的二进制形式的最高位遍历到最低位
            cur_bit = (idx >> (h - 2 - depth)) & 1
            if cur_bit == 1:
                node = node.right
            else:
                node = node.left
        return node is not None

    def exist2(self, root: TreeNode, h: int, idx: int) -> bool:
        """
        另一种写法，用一个二进制 mask 来获得位信息，而不用每次计算 bit
        """
        node = root

        # 将 001 向左位移 h-2， 假设 h为4， 则左移2位得到 100 代表最高位的 mask
        mask = 1 << (h - 2)
        for _ in range(h - 1):
            if idx & mask:  # 当前 mask 所在的二进制位置为 1
                node = node.left
            else:
                node = node.right

            mask >>= 1  # 向右移动一位，开始看下一个位置
        return node is not None

    def countNodes(self, root: TreeNode | None) -> int:
        """
        时间复杂度能否优化？
        先计算完全二叉树高度 h, 然后计算最后一层结点个数
        关键问题是 如何在 小于 O(N) 复杂度的时间内计算最后一层结点个数呢？
        给完全二叉树按层次遍历进行编号(根结点为第一层，最底层为h层，编号从1开始)可知
        最后一层的编号范围在 [2^{h-1}, 2^h-1]，二叉树搜索一个结点的时间复杂度为 O(logN)
        因此可以通过二分查找，来找到最大编号的结点

        时间复杂度 = O(logN) 计算树高 + O(logN) 二分查找编号 * O(logN) 查找对应编号的结点是否存在 = O((logN)^2)
        """
        if not root:
            return 0

        # 计算树高
        h = self.get_height(root)

        # 二分查找, 最后需要右指针指向最后一个存在的结点
        left = 0
        right = 2 ** (h - 1) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.exist(root, h, mid):
                left = mid + 1
            else:
                right = mid - 1
        return 2 ** (h - 1) - 1 + right + 1

    def countNodesV1(self, root: TreeNode | None) -> int:
        """
        直接遍历记数，O(N) 复杂度
        """
        self.num_nodes = 0

        def preorder(node):
            if node is None:
                return
            self.num_nodes += 1
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return self.num_nodes


def construct_tree(level_order):
    if not level_order: return None
    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()

        if level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1

    return root


def level_order(root):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            res.append(None)
            continue

        res.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    # 去掉末尾多余的 None
    while res and res[-1] is None:
        res.pop()

    return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13),
        ([1, 2, 3, 4, 5, 6], 6),
        ([1, 2, 3, 4, 5, 6, 7], 7),
        ([1, 2, 3], 3),
        ([], 0),
        ([1], 1)
    ]
    for case in cases:
        root = construct_tree(case[0])
        print(level_order(root))
        res = solution.countNodes(root)
        print(res, case[-1])
