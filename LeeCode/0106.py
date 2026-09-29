from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int], ) -> TreeNode | None:
        """
        后序与中序序列构造二叉树，核心在于找到 postorder 和 inorder 的递归结构
        当前 root 在 postorder 的位置为 -1, 在 inorder 的位置为 i
        则左子树可以通过 inorder[:i] 和 postorder[:i] 来构建
        则右子树可以通过 inorder[i+1:] 和 postorder[i:-1] 来构建
        """
        if not postorder or not inorder:
            return None

        node = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        left_tree = self.buildTree(inorder[:idx], postorder[:idx])
        right_tree = self.buildTree(inorder[idx + 1:], postorder[idx:-1])
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
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1])
    ]
    for case in cases:
        res = solution.buildTree(case[0], case[1])
        res = level_order(res)
        print(res, case[-1])
