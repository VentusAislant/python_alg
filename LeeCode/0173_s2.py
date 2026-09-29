from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """
    二叉搜索树的中序遍历序列正好是升序序列

    二叉搜索树迭代器，核心是不能一次获得所有元素，必须迭代获得
        __init__: 传入的 root 是根据序列构建好的二叉搜索树的根结点
        hasNext 如果当前迭代器指针 next 存在数字，则返回 True, 否则返回False
        next 将指针向右移动，然后返回指针处的数字

    利用一个栈保存当前的结点的所有左链，及当前结点，
    每次 next 弹出栈顶，即最小的元素，如果弹出的结点有右孩子，则压入右孩子左链
    """

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        """将左孩子链压入栈"""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

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


if __name__ == '__main__':
    cases = [
        (
            ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
            [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []],
            [None, 3, 7, True, 9, True, 15, True, 20, False],
        )
    ]
    for case in cases:
        bsti = None
        res = []
        for op, arg in zip(*case[:-1]):
            if op == "BSTIterator":

                bsti = BSTIterator(construct_tree(*arg))
                res.append(None)
            elif op == "next":
                res.append(bsti.next())
            elif op == "hasNext":
                res.append(bsti.hasNext())

        print(res, case[-1])
