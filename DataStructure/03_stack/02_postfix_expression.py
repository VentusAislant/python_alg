# 逆波兰表达式/后缀表达式：
# 1. 中缀表达式转后缀表达式
# 2. 后缀表达式计算

def infix2postfix(expression) -> list[str]:
    """
    中缀表达式转后缀表达式，支持加减乘除和多位数字
    :param expression: 中缀表达式
    :return: 后缀表达式
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    operator_stack = []
    output_list = []

    def is_operator(c):
        return c in precedence

    def not_higher_precedence(op1, op2):
        return precedence[op1] <= precedence[op2]

    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isdigit():
            # 如果是数字则添加到输出列表，需要处理多位数的情况
            num = ''
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            output_list.append(num)
            continue  # 避免最后的 i+=1
        elif char == '(':
            # 左括号直接入栈
            operator_stack.append(char)
        elif char == ')':
            # 右括号需要出栈， 出到左括号
            while operator_stack and operator_stack[-1] != '(':
                output_list.append(operator_stack.pop())
            # 弹出左括号
            operator_stack.pop()
        elif is_operator(char):
            # 如果当前操作符的优先级小于等于栈顶运算符的优先级则需要进行出栈
            while operator_stack and operator_stack[-1] != '(' and \
                    not_higher_precedence(char, operator_stack[-1]):
                output_list.append(operator_stack.pop())
            operator_stack.append(char)
        i+=1

    while operator_stack:
        output_list.append(operator_stack.pop())
    return output_list


def evaluate_postfix(postfix: list) -> float|int:
    """
    计算后缀表达式的值
    :param postfix: 后缀表达式列表
    :return: 后缀表达式计算得到的值
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    num_stack = []
    i = 0
    while i < len(postfix):
        char = postfix[i]
        if char not in precedence.keys():
            num_stack.append(float(char))
        else:
            # 取出前两个运算数进行运算, 然后压入栈
            num_b, num_a = num_stack.pop(), num_stack.pop()
            if char == '+':
                cur_val = num_a + num_b
            elif char == '-':
                cur_val = num_a - num_b
            elif char == '*':
                cur_val = num_a * num_b
            elif char == '/':
                cur_val = num_a / num_b
            else:
                raise ValueError(f'Not Supported {char}')
            num_stack.append(cur_val)
        i+=1
    assert len(num_stack) == 1
    result = num_stack[-1]
    return int(result) if result == int(result) else result



if __name__ == '__main__':
    infix_str = '(333*4+6)*5-3'
    postfix_str = infix2postfix(infix_str)
    print(postfix_str)
    val = evaluate_postfix(postfix_str)
    print(val)