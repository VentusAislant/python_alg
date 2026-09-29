import heapq


class MedianFinder:
    """
    数据流中位数类，数据来流过程中，始终能获得中位数字
    void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
    double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
    """

    def __init__(self):
        """
        中位数的一个关键性质就是，在中间位置，左边元素小于他，右边元素大于他，可以用两个堆来分别存储左右边元素
        左边较小的元素用一个大根堆，可以很快找到最右边元素
        右边较大的元素用一个小根堆，可以很快找到最左边的元素

        需要关注的是在插入过程中需要保证两个堆平衡，并且左边的堆的最大元素 <= 右边的堆的最小元素

        left_heap 最多比 right_heap 多一个元素
        """
        self.left_heap = []  # 大根堆
        self.right_heap = []  # 小根堆

    def addNum(self, num: int) -> None:
        # 先放入 left_heap
        heapq.heappush(self.left_heap, -num)

        # 保证两个堆的性质，left_heap 的最大 <= right_heap 的最小
        if self.right_heap and -self.left_heap[0] > self.right_heap[0]:
            element = - heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, element)

        # 保证两个堆的平衡
        if len(self.left_heap) - len(self.right_heap) > 1:
            element = - heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, element)
        elif len(self.right_heap) > len(self.left_heap):
            element = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -element)

    def findMedian(self) -> float:
        if len(self.left_heap) > len(self.right_heap):
            return - float(self.left_heap[0])
        else:
            return (- self.left_heap[0] + self.right_heap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == '__main__':
    cases = [
        (
            ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [1], [2], [], [3], []],
            [None, None, None, 1.5, None, 2.0]
        )
    ]
    for case in cases:
        mf = None
        res = []
        for op, args in zip(*case[:-1]):
            if op == "MedianFinder":
                mf = MedianFinder()
                res.append(None)
            elif op == "addNum":
                mf.addNum(*args)
                res.append(None)
            elif op == "findMedian":
                res.append(mf.findMedian())

        print(res, case[-1])
