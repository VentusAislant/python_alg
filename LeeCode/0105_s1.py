from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """
        前序与中序序列构造二叉树，核心在于找到 preorder 和 inorder 的递归结构
        当前 root 在 preorder 的位置为 0, 在 inorder 的位置为 j
        则左子树可以通过 inorder[:j] 和 preorder[1:j+1] 来构建
        则右子树可以通过 inorder[j+1:] 和 preorder[j+1:] 来构建
        """
        if not preorder or not inorder:
            return None

        node = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        left_tree = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        right_tree = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        node.left = left_tree
        node.right = right_tree
        return node


def level_order(root: TreeNode) -> list[int | None]:
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)

    # 去掉末尾多余的 None
    while res and res[-1] is None:
        res.pop()
    return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1])
    ]
    for case in cases:
        res = solution.buildTree(case[0], case[1])
        res = level_order(res)
        print(res, case[-1])
