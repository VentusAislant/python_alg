from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
        """
        问题本质，找到一棵树，根结点是 p 和 q 的最近公共祖先
        递归思想: 对于 root，p,q只能出现三种情况之一
            1. p 和 q 分别在左右子树： root 就是 p 和 q 的最近公共祖先
            2. p 和 q 都在左子树：  p 和 q 的最近公共祖先在 root 的左子树
            3. p 和 q 都在右子树： p 和 q 的最近公共左先在 root 的右子树

        因此可以用递归算法来实现
            递归终止条件：
                当前结点为空, 返回 None
                当前结点是 p 或 q， 返回当前结点
           递归左右子树
                left_ancestor = lowestCommonAncestor(root.left, p, q)
                right_ancestor = lowestCommonAncestor(root.right, p, q)
            合并左右结果
                left_ancestor， right_ancestor 都非 None,说明 p,q分别在左右子树，返回 root
                left_ancestor， right_ancestor 其中一个为 None,说明 p,q 在左子树或右子树，返回 不为空的左右子树
        """
        if root is None:
            return None

        if p is root or q is root:
            return root

        left_ancestor = self.lowestCommonAncestor(root.left, p, q)
        right_ancestor = self.lowestCommonAncestor(root.right, p, q)
        if left_ancestor and right_ancestor:
            return root
        else:
            return left_ancestor if left_ancestor else right_ancestor


def construct_tree(level_order):
    queue = deque()
    root = TreeNode(level_order[0])
    queue.append(root)
    i = 1
    while queue:
        node = queue.popleft()
        if i < len(level_order):
            node.left = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.left)
            i += 1
        if i < len(level_order):
            node.right = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.right)
            i += 1
    return root


def level_order(root: TreeNode) -> List[Optional[int]]:
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
    ]
    for case in cases:
        tree = construct_tree(case[0])
        res = solution.lowestCommonAncestor(tree, case[1], case[2])
        print(res, case[-1])
