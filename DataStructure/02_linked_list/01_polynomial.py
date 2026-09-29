class PNode:
    """
    多项式节点类
        coefficient: 系数
        exponent: 次幂
        _next: 指针
    """

    def __init__(self, coefficient, exponent, _next=None):
        self.coefficient = coefficient
        self.exponent = exponent
        self._next = _next


class Polynomial:
    """
    多项式类
    """

    def __init__(self, coefficients: tuple | list = (), exponents: tuple | list = ()):
        self.head = PNode(None, None)  # 头节点
        self._create(coefficients, exponents)

    def is_empty(self):
        if self.head._next is None:
            return True
        else:
            return False

    def _create(self, coefficients, exponents):
        if len(coefficients) != len(exponents):
            raise ValueError("coefficients and exponents must have same length")
        if len(coefficients) == 0:
            return

        # 先将指数和系数构建成二元组，然后根据二元组中的指数进行排序
        data = [(coefficients[i], exponents[i]) for i in range(len(coefficients))]
        data.sort(key=lambda x: x[1])

        cur_node = self.head
        for item in data:
            cur_node._next = PNode(item[0], item[1])
            cur_node = cur_node._next

    def __add__(self, other):
        # 多项式相加: 将自己的 head 之后断开，遍历两个链表进行插入，加到自己链表中
        p, q = self.head._next, other.head._next
        result = Polynomial()
        cur_node = result.head
        while p is not None and q is not None:
            if p.exponent == q.exponent:
                cur_coef = p.coefficient + q.coefficient
                if cur_coef != 0:
                    cur_node._next = PNode(cur_coef, p.exponent)
                    cur_node = cur_node._next
                p = p._next
                q = q._next
            elif p.exponent < q.exponent:
                cur_node._next = PNode(p.coefficient, p.exponent)
                cur_node = cur_node._next
                p = p._next
            else:
                cur_node._next = PNode(q.coefficient, q.exponent)
                cur_node = cur_node._next
                q = q._next

        while p:
            cur_node._next = PNode(p.coefficient, p.exponent)
            cur_node = cur_node._next
            p = p._next

        while q:
            cur_node._next = PNode(q.coefficient, q.exponent)
            cur_node = cur_node._next
            q = q._next
        return result

    def __iadd__(self, other):
        result = self + other
        self.head._next = result.head._next
        return self

    def __str__(self):
        print_str = f"[Polynomial]: "
        if self.head._next is not None:
            print_str += 'head -> '
        else:
            print_str += 'head'

        cur_node = self.head
        while cur_node._next is not None:
            cur_node = cur_node._next
            print_str += f"{cur_node.coefficient} "
            if cur_node.exponent != 0:
                print_str += f"* x^{cur_node.exponent} "
            if cur_node._next is not None:
                print_str += '+ '
        return print_str

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    # 1 - x
    p1 = Polynomial(
        coefficients=(1, -1),
        exponents=(0, 1),
    )

    # 1 + x + x^2
    p2 = Polynomial(
        coefficients=(1, 1, 1),
        exponents=(2, 1, 0),
    )
    print(p2)
    print(p1)
    print(p1 + p2)
