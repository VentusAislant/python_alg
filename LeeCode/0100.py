from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        两个同时遍历即可，必须当前结点和左右子树都完全相同才是相同
        """
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


def construct_tree(level_order) -> TreeNode:
    """
    层序遍历序列构建二叉树：
        使用队列辅助，首先根结点入队
        每次取出一个结点，构建其左右子结点，构建完毕后左右子结点入队
    """
    queue = deque()
    root = TreeNode(level_order[0])
    queue.append(root)
    i = 1
    while queue and i < len(level_order):
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


if __name__ == '__main__':
    cases = [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
    ]

    solution = Solution()
    for p, q, answer in cases:
        p_tree = construct_tree(p)
        q_tree = construct_tree(q)
        output = solution.isSameTree(p_tree, q_tree)
        print(answer, output)
