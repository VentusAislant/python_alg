from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        """
        前缀和思路
            先以数组为例，给定一个数组 [1, 2, 3, 4, 5] 求数组和为 k 的子数组数量，怎么数？
            最经典的思路是用前缀和，记录每一个位置的前缀和 prefix_sum = [1, 3, 6, 10, 15]
            此时位置 i 到 位置 j 的和就可以通过前缀和数组 prefix_sum[j] - prefix_sum[i] 计算

            对于树来说，只需要记录所有出现过的前缀和的次数，每次到一个结点判断以当前结点结尾的符合条件的路径和数量即可
        """
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node: TreeNode, cur_sum: int):
            if node is None:
                return 0

            # 更新前缀和
            cur_sum += node.val

            # 把当前前缀和加入路径
            prefix[cur_sum] += 1

            # 统计以当前结点结尾的满足要求的路径数量
            # cur_sum - pre_sum = target_sum
            # pre_sum = cur_sum - target_sum  # 要寻找前缀和等于 pre_sum 的路径数量
            res = prefix[cur_sum - targetSum]


            # 递归
            res += dfs(node.left, cur_sum)
            res += dfs(node.right, cur_sum)

            # 回溯（移除当前结点）
            prefix[cur_sum] -= 1  # 避免路径跨越左右子树
            return res

        return dfs(root, 0)

    def pathSumV1(self, root: TreeNode | None, targetSum: int) -> int:
        """
        递归思路，需要两层递归，内层递归计算，从一个结点出发的满足 targetSum 的路径数量
        外层递归，计算所有结点
        """
        if root is None:
            return 0

        def inner_dfs(node, cur_sum=0) -> int:
            """
            可以计算从任意结点出发的满足 targetSum 的路径数量
            """
            if node is None:
                return 0
            cur_sum += node.val
            cnt = 1 if cur_sum == targetSum else 0
            cnt += inner_dfs(node.left, cur_sum)
            cnt += inner_dfs(node.right, cur_sum)
            return cnt

        # 外层递归
        res = inner_dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        return res


def construct_tree(level_order):
    if len(level_order) == 0:
        return None
    queue = deque()
    root = TreeNode(level_order[0])
    queue.append(root)
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if i < len(level_order) and node:
            node.left = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.left)
            i += 1

        if i < len(level_order) and node:
            node.right = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.right)
            i += 1
    return root


def level_order(root: TreeNode | None) -> list[int]:
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == '__main__':
    cases = [
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3)
    ]
    solution = Solution()
    for case in cases:
        tree = construct_tree(case[0])
        res = solution.pathSum(tree, case[1])
        print(res, case[2])
