from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        """
        BST 的中序遍历是一个升序序列，因此可以中序遍历，过程中用 pre 记录前一个访问的结点
        利用 pre 和 当前结点计算的差值可能是最小绝对差值，再用一个全局变量 min_diff 保存最小绝对差即可
        """
        self.min_diff = float('inf')
        self.pre = None

        def inorder(node):
            if node is None:
                return

            if node.left:
                inorder(node.left)

            if self.pre:
                self.min_diff = min(self.min_diff, abs(node.val - self.pre.val))
            self.pre = node

            if node.right:
                inorder(node.right)

        inorder(root)
        return self.min_diff


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
        ([1, 0, 48, None, None, 12, 49], 1),
    ]
    for case in cases:
        tree = construct_tree(case[0])
        res = solution.getMinimumDifference(tree)
        print(res, case[-1])
