from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        能不能不使用额外空间，即不使用层次遍历？
        可以发现上一层结点构建的 next 链，可以方便进行下一层所有结点的访问和构造链
        利用这个特点可以实现 O(1) 空间的算法实现
        """
        if not root:
            return root

        cur = root
        while cur:
            next_head = None  # 下一层的起点
            next_pre = None  # 辅助构造当前层 next 链

            # 遍历当前层（从左向右）
            while cur:
                for child in (cur.left, cur.right):
                    if child:
                        if not next_head:
                            next_head = child  # 记录下一层的开始结点
                        if next_pre is not None:
                            next_pre.next = child
                        next_pre = child

                cur = cur.next  # 当前层向右

            cur = next_head  # 下一层
        return root

    def connectV2(self, root: 'Node') -> 'Node':
        """
        每一层的结点从左至右需要串联起来
        可以使用层序遍历，每次直接遍历一层，将一层的结点用 next 串联
        使用一个 pre 变量存储每一层的前一个结点，避免使用数组
        """
        if not root:
            return root

        queue = deque([root])
        while queue:
            cur_layer_size = len(queue)
            pre = None
            for _ in range(cur_layer_size):
                cur_layer_node = queue.popleft()

                if pre is None:
                    pre = cur_layer_node
                else:
                    pre.next = cur_layer_node
                    pre = cur_layer_node

                if cur_layer_node.left:
                    queue.append(cur_layer_node.left)
                if cur_layer_node.right:
                    queue.append(cur_layer_node.right)

        return root

    def connectV1(self, root: 'Node') -> 'Node':
        """
        每一层的结点从左至右需要串联起来
        可以使用层序遍历，每次直接遍历一层，将一层的结点用 next 串联
        """
        if not root:
            return root

        queue = deque([root])
        while queue:
            cur_layer_size = len(queue)
            cur_layer_nodes = []
            for _ in range(cur_layer_size):
                cur_layer_node = queue.popleft()
                cur_layer_nodes.append(cur_layer_node)
                if cur_layer_node.left:
                    queue.append(cur_layer_node.left)
                if cur_layer_node.right:
                    queue.append(cur_layer_node.right)

            for i in range(len(cur_layer_nodes) - 1):
                cur_layer_nodes[i].next = cur_layer_nodes[i + 1]
        return root


def construct_tree(level_order):
    if not level_order:
        return None
    queue = deque()
    root = Node(level_order[0])
    queue.append(root)
    i = 1
    while queue:
        node = queue.popleft()
        if i < len(level_order):
            node.left = Node(level_order[i]) if level_order[i] is not None else None
            queue.append(node.left)
            i += 1
        if i < len(level_order):
            node.right = Node(level_order[i]) if level_order[i] is not None else None
            queue.append(node.right)
            i += 1
    return root


def level_order_with_next(root: 'Node') -> list[int | str | None]:
    if not root:
        return []
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        cur_layer_size = len(queue)
        for _ in range(cur_layer_size):
            node = queue.popleft()
            res.append(node.val if node is not None else None)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append('#')

    # 去掉末尾多余的 None
    while res and res[-1] is None:
        res.pop()
    return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1, 2, 3, 4, 5, None, 7], [1, '#', 2, 3, '#', 4, 5, 7, '#']),
        ([], [])
    ]
    for case in cases:
        tree = construct_tree(case[0])
        res = solution.connect(tree)
        res = level_order_with_next(res)
        print(res, case[-1])
