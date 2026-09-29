class MinStack:
    """
    最简单的思路，用一个变量记录当前最小值，但是 pop 操作可能会 pop 掉 当前最小值，更新最小值需要 O(N)复杂度

    改进：
        使用一个辅助栈来记录最小值, 因为栈是先进先出，每个时刻栈内元素固定，因此最小值也是固定
        所以可以辅助栈和主栈同步，主栈压入val,辅助栈压入当前最小值，主栈和辅助栈同时 pop 即可
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            cur_min = self.min_stack[-1] if self.min_stack[-1] < val else val
            self.min_stack.append(cur_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    cases = [
        (
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []],
            [None, None, None, None, -3, None, 0, -2]
        )
    ]
    min_stack = None
    for case in cases:
        cur_res = []
        for op, args in zip(*case[:-1]):
            if op == "MinStack":
                min_stack = MinStack()
                cur_res.append(None)
            elif op == "push":
                min_stack.push(*args)
                cur_res.append(None)
            elif op == "getMin":
                cur_res.append(min_stack.getMin())
            elif op == "pop":
                min_stack.pop()
                cur_res.append(None)
            elif op == "top":
                cur_res.append(min_stack.top())
            else:
                raise ValueError

        print(cur_res, case[-1])
