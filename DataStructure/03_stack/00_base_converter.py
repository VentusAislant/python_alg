"""
- 栈是只允许在一端进行插入和删除的线性表。后进先出(Last In First Out, LIFO)
- 栈顶：是栈允许插入和删除元素的一端。栈底：固定的，不允许插入和删除的一端
- 空栈：不含任何数据元素的栈
- 含有n个不同元素的栈的合法出栈序列个数：卡特兰数 $\frac{1}{n+1} C_{2n}^{n}$
- 栈可以用顺序表或者链表来实现，Python 中的 list 已经实现了栈的功能，可以直接拿来使用
"""
# 使用栈实现进制转化

class BaseConverter:
    """
    十进制转任意进制
    """
    def __init__(self, target_base=16):
        self.target_base = target_base
        self.digit_map = "0123456789ABCDEF"

        self.prefix = f'target base <{self.target_base}>: '
        if self.target_base == 16:
            self.prefix = '0x'
        elif self.target_base == 8:
            self.prefix = '0o'
        elif self.target_base == 2:
            self.prefix = '0b'


    def __call__(self, number):
        stack = []
        target_number_str = self.prefix
        while number != 0:
            cur_digit = number % self.target_base
            stack.append(cur_digit)
            number //= self.target_base
        while len(stack) > 0:
            cur_digit = stack.pop()
            target_number_str += self.digit_map[cur_digit]
        return target_number_str

if __name__ == '__main__':
    base_converter = BaseConverter(target_base=16)
    print(base_converter(255))  # 0xFF