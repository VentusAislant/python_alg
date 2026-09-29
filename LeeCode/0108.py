class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        """
        由于是升序数组，所以直接拿中间的数当作根，然后左边区间构建左子树，右边区间构建右子树即可
        """
        if not nums:
            return None

        left, right = 0, len(nums)
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


def get_level_order(root: TreeNode) -> list:
    if not root:
        return []

    from collections import deque
    queue = deque([root])
    res = []
    while queue:
        node = queue.popleft()
        if node is not None:
            res.append(node.val)
            if node.left is not None or node.right is not None:
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
        (
            [-10, -3, 0, 5, 9],
            [0, -3, 9, -10, None, 5]
        ),
        (
            [1, 3],
            [3, 1]
        )
    ]
    for case in cases:
        tree = solution.sortedArrayToBST(*case[:-1])
        res = get_level_order(tree)
        print(res, case[-1])
