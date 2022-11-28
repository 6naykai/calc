import math

import const

const.EmptyTOS = -1
const.MinStackSize = 5


class stack(object):
    def __init__(self):
        self.top = const.EmptyTOS
        self.cap = const.MinStackSize
        self.listarray = []

    # 判断栈是否为空(bool)
    def isEmpty(self):
        return self.top == const.EmptyTOS

    # 判断栈是否满了(bool)
    def isFull(self):
        return self.top + 1 == self.cap

    # push操作,向栈内堆入元素
    def push(self, item):
        if self.isFull():
            self.cap = self.cap * 2
        self.top += 1
        self.listarray.append(item)

    # pop操作,将栈顶元素移除
    def pop(self):
        self.listarray.pop()
        self.top -= 1

    # peek操作,取出栈顶元素
    def peek(self):
        if not self.isEmpty():
            return self.listarray[self.top]

    # 返回栈内数据总量(int)
    def size(self):
        return len(self.listarray)


# 区分数字与运算符(bool型),若是运算符则返回TRUE
def identify_ope(ope):
    if ope == '+':
        return True
    if ope == '-':
        return True
    if ope == '×':
        return True
    if ope == '÷':
        return True
    if ope == '(':
        return True
    if ope == ')':
        return True
    if ope == '%':
        return True
    if ope == 'sqrt':
        return True
    if ope == '^':
        return True
    return False


# 区分数字与运算符(bool型),若是数字则返回TRUE
def identify_num(num):
    if num == '0':
        return True
    if num == '1':
        return True
    if num == '2':
        return True
    if num == '3':
        return True
    if num == '4':
        return True
    if num == '5':
        return True
    if num == '6':
        return True
    if num == '7':
        return True
    if num == '8':
        return True
    if num == '9':
        return True
    if num == '.':
        return True
    return False


# 判断括号合法性(bool),括号不合法则输出False
def brackets_legal(infix_stack):
    brackets_stack = stack()
    size = infix_stack.size()
    for i in range(size):
        if infix_stack.listarray[i] == '(':
            brackets_stack.push(item='(')
        if infix_stack.listarray[i] == ')':
            if brackets_stack.isEmpty():
                return False
            else:
                brackets_stack.pop()
    if brackets_stack.isEmpty():
        return True
    return False


# 将运算表达式放入中缀表达式栈中(stack型)
def infix(text):
    infix_stack = stack()
    size = len(text)
    num = ''
    sqrt = ''  # 用于存放sqrt
    for i in range(size):
        # 判断当前选中字符是否为数字或小数点,若是则存入num中
        if identify_num(text[i]):
            num += text[i]
        # 如果当前选中字符是sqrt的元素,则将其存入sqrt中
        elif text[i] == 's' or text[i] == 'q' or text[i] == 'r' or text[i] == 't':
            sqrt += text[i]
        else:
            # 若sqrt存满,则将sqrt堆入栈中,并将sqrt初始化
            if sqrt == 'sqrt':
                infix_stack.push(item=sqrt)
                sqrt = ''
            # 若num中存有数字则将其转化为float型,堆入栈中
            if num != '':
                infix_stack.push(item=float(num))
                num = ''
            # 将当前运算符堆入栈中
            infix_stack.push(item=text[i])
    # 若最后num中还存有数字,则堆入栈中
    if num != '':
        infix_stack.push(item=float(num))
    # 返回中缀栈
    return infix_stack


# 将中缀表达式栈转化为后缀表达式栈(stack型)
def infix_to_suffix(infix_stack):
    suffix_stack = stack()  # 后缀表达式栈
    ope = stack()  # 运算符栈(中间栈)
    size = infix_stack.size()  # 中缀表达式栈的大小
    flag = 1
    for i in range(size):
        temp = infix_stack.listarray[i]
        # 若栈当前元素是数字,则直接压入后缀表达式栈中
        if not identify_ope(temp):
            suffix_stack.push(item=temp)
        # 左括号'('优先级最高,直接入运算符栈
        if temp == '(':
            ope.push(item=temp)
        # 如果是'+'、'-'、'×'、'÷'、'sqrt'根据算数符号优先级入栈
        if temp == '+' or temp == '×' or temp == '-' or temp == '÷' or temp == 'sqrt' or temp == '^':
            # 若运算符栈空,则算数符号入栈
            if ope.isEmpty():
                ope.push(item=temp)
            # 否则,根据算数符号优先级入栈与出栈
            else:
                while True:
                    # 取出栈顶算数符号
                    ope_top = ope.peek()
                    # 若运算符栈顶算术符号优先级低于当前算术符号,则直接入运算符栈
                    if priority(temp, ope_top):
                        ope.push(item=temp)
                        break
                    # 否则,运算符栈顶算术符号压入后缀表达式栈中
                    else:
                        suffix_stack.push(item=ope_top)
                        ope.pop()  # 算数符号出运算符栈直到当前算术符号优先级大于运算符栈栈顶算术符号
                        # 如果栈空,那么当前算数符号入栈
                        if ope.isEmpty():
                            ope.push(item=temp)
                            break
        # 如果栈当前元素是右括号')',算数符号出运算符栈,直到遇到左括号'('为止
        if temp == ')':
            while ope.peek() != '(':
                suffix_stack.push(item=ope.peek())
                ope.pop()
            ope.pop()  # '('出栈,且不放入算数表达式
    # 运算符栈中剩余算术符号压入后缀表达式栈中
    while not ope.isEmpty():
        suffix_stack.push(item=ope.peek())
        ope.pop()
    # 返回后缀表达式栈
    return suffix_stack


# 利用后缀表达式栈计算后缀表达式结果(float型)
def compute_suffix(suffix_stack):
    num = stack()  # 数字栈
    size = suffix_stack.size()  # 后缀表达式栈的大小
    for i in range(size):
        temp = suffix_stack.listarray[i]
        # 数字直接入栈
        if not identify_ope(temp):
            num.push(item=temp)
        # 执行加法'+'
        if temp == '+':
            b = num.peek()
            num.pop()
            a = num.peek()
            if a is None:
                num.push(item=float(b))
                continue
            num.pop()
            num.push(item=float(a + b))
        # 执行减法'-'
        if temp == '-':
            b = num.peek()
            num.pop()
            a = num.peek()
            if a is None:
                num.push(item=float(-b))
                continue
            num.pop()
            num.push(item=float(a - b))
        # 执行乘法'×'
        if temp == '×':
            b = num.peek()
            num.pop()
            a = num.peek()
            num.pop()
            num.push(item=float(a * b))
        # 执行除法'÷'
        if temp == '÷':
            b = num.peek()
            num.pop()
            a = num.peek()
            num.pop()
            num.push(item=float(a / b))
        # 执行开方运算'sqrt'
        if temp == 'sqrt':
            a = num.peek()
            num.pop()
            num.push(item=math.sqrt(a))
        # 执行幂运算'^'
        if temp == '^':
            b = num.peek()
            num.pop()
            a = num.peek()
            num.pop()
            num.push(item=pow(a, b))
    if num.size() == 1:
        return num.peek()  # 返回后缀表达式结果
    raise Exception


# 中缀表达式改写后缀表达式
def InfixToSuffix(text):
    st = stack()
    res = str()
    size = len(text)
    for i in range(size):
        # 数字直接放入算术表达式
        if text[i] != '(' and text[i] != ')' and text[i] != '+' and text[i] != '*' and text[i] != '-':
            res += text[i]
        # 左括号'('优先级最高,直接入栈
        if text[i] == '(':
            st.push(item=text[i])
        # 如果是'+'、'-'、'*'根据算数符号优先级入栈
        if text[i] == '+' or text[i] == '*' or text[i] == '-':
            # 栈空,算数符号入栈;否则,根据算数符号优先级出栈
            if st.isEmpty():
                st.push(item=text[i])
            # 否则,根据算数符号优先级入栈
            else:
                while True:
                    # 取出栈顶算数符号
                    temp = st.peek()
                    # 若栈顶算术符号优先级高于当前算术符号,则直接入栈
                    if priority(text[i], temp):
                        st.push(item=text[i])
                        break
                    # 否则,栈顶算术符号放入算术表达式
                    else:
                        res += temp
                        st.pop()  # 算数符号出栈直到当前算术符号优先级大于栈顶算术符号
                        # 如果栈空,那么当前算数符号入栈
                        if st.isEmpty():
                            st.push(item=text[i])
                            break
        # 如果是右括号')',算数符号出栈,直到遇到左括号'('为止
        if text[i] == ')':
            while st.peek() != '(':
                res += st.peek()
                st.pop()
            st.pop()  # '('出栈,且不放入算数表达式
    # 栈中剩余算术符号放入算术表达式
    while not st.isEmpty():
        res += st.peek()
        st.pop()
    return res


# 计算后缀表达式
def compute(text):
    st = stack()
    size = len(text)
    for i in range(size):
        # 数字直接入栈,注意str转化为int
        if text[i] != '(' and text[i] != ')' and text[i] != '+' and text[i] != '*' and text[i] != '-':
            st.push(item=int(text[i]))
        # 执行加法'+'
        if text[i] == '+':
            b = st.peek()
            st.pop()
            a = st.peek()
            st.pop()
            st.push(item=a + b)
        # 执行减法'-'
        if text[i] == '-':
            b = st.peek()
            st.pop()
            a = st.peek()
            st.pop()
            st.push(item=a - b)
        # 执行乘法'*'
        if text[i] == '*':
            b = st.peek()
            st.pop()
            a = st.peek()
            st.pop()
            st.push(item=a * b)
    return st.peek()  # 返回后缀表达式结果


# 算数符号优先度(int型)
def symbol_priority(symbol):
    # 定义在栈中左括号的优先度为0
    if symbol == '(':
        return 0
    # 定义加减运算的优先度为1
    if symbol == '+' or symbol == '-':
        return 1
    # 定义乘除运算的优先度为2
    if symbol == '×' or symbol == '÷':
        return 2
    # 定义sqrt运算的优先度为3
    if symbol == 'sqrt' or symbol == '^':
        return 3


# 算术优先级判断(bool型)
def priority(a, b):
    # 算术优先级a > b,则返回true
    return symbol_priority(a) > symbol_priority(b)

    # # 算数加法
    # if a == '+' and b == '+':
    #     return False
    # if a == '+' and b == '*':
    #     return False
    # if a == '+' and b == '(':
    #     return True
    # if a == '+' and b == '-':
    #     return False
    # if a == '+' and b == '/':
    #     return False
    # # 算数减法
    # if a == '-' and b == '+':
    #     return False
    # if a == '-' and b == '-':
    #     return False
    # if a == '-' and b == '*':
    #     return False
    # if a == '-' and b == '(':
    #     return True
    # if a == '-' and b == '/':
    #     return False
    # # 算数乘法
    # if a == '*' and b == '+':
    #     return True
    # if a == '*' and b == '-':
    #     return True
    # if a == '*' and b == '*':
    #     return False
    # if a == '*' and b == '(':
    #     return True
    # if a == '*' and b == '/':
    #     return False
    # # 算数除法
    # if a == '/' and b == '+':
    #     return True
    # if a == '/' and b == '-':
    #     return True
    # if a == '/' and b == '*':
    #     return False
    # if a == '/' and b == '(':
    #     return True
    # if a == '/' and b == '/':
    #     return False
    # return False  # 语法要求必有返回值
