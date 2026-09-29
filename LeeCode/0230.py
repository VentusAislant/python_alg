from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        容易弄错的做法是：只递归判断当前结点和左右子结点的大小，没有考虑全局关系
        例如:
                5
               / \
              1   7
                 / \
                3   8     这里的 3 是不符合 BST 规则的， 3应该在左子树

        可以采用区间递归法，假设当前结点值为 k, 那么左子树的范围必须在 (-inf, k), 右子树 (k, inf)
        """

        def validate(node, low=float('-inf'), high=float('inf')) -> bool:
            if node is None:
                return True

            if node.val >= high or node.val <= low:
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root)


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
        ([5, 1, 4, None, None, 3, 6], False),
        ([2, 1, 3], True),
        ([5, 4, 6, None, None, 3, 7], False),
    ]
    for case in cases:
        tree = construct_tree(case[0])
        res = solution.isValidBST(tree)
        print(res, case[-1])
