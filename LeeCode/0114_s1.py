from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        可以使用一个 pre 变量保存上一个访问的结点，然后利用 pre 在前序遍历的过程中进行展开
        但是这种不适用于递归的前序遍历实现, 递归实现过程中会修改结点 right 指针，导致递归结构出错
        使用迭代的方法
        """
        if not root:
            return

        stack = [root]
        pre = None

        while stack:
            cur = stack.pop()

            if pre:
                pre.left = None
                pre.right = cur

            # 因为栈后进先出，所以需要先压入右，再压入左
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

            # 左右结点可以先压入栈，结构不会改变
            pre = cur
        return None

    def flattenV1(self, root: TreeNode | None) -> None:
        """
        前序遍历二叉树，然后用一个列表记录前序序列，之后利用列表进行展开
        """
        if not root:
            return

        node_lst = []

        def preorder(node, lst):
            if not node:
                return None

            lst.append(node)
            preorder(node.left, lst)
            preorder(node.right, lst)

        preorder(root, node_lst)

        for i in range(len(node_lst) - 1):
            node_lst[i].right = node_lst[i + 1]
            node_lst[i].left = None

        return None


def construct_tree(level_order):
    if not level_order: return None
    root = TreeNode(level_order[0])
    queue = deque()
    queue.append(root)
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if i < len(level_order):
            node.left = TreeNode(level_order[i]) if level_order[i] is not None else None
            i += 1
            queue.append(node.left)

        if i < len(level_order):
            node.right = TreeNode(level_order[i]) if level_order[i] is not None else None
            i += 1
            queue.append(node.right)
    return root


def level_order(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        node = queue.popleft()
        if node is not None:
            res.append(node.val)
            # 无论左右是否为 None，都入队
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)

    # 去掉末尾多余的None
    while res and res[-1] is None:
        res.pop()
    return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
        ([], []),
        ([0], [0])
    ]
    for case in cases:
        root = construct_tree(case[0])
        solution.flatten(root)
        print(level_order(root), case[-1])
