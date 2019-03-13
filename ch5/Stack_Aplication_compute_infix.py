####################################################################################
#法1：利用后缀表达式计算来实现
#输入：以空白作为分隔
#输出：一个计算结果
###################################################################################
#line = input('Infix Expression: ')
line = '( ( 1 + 2 ) * ( 3 + 4 ) - 27 ) / ( 2 + 1 )'
value = suf_exp_evaluator(trans_infix_suffix(line))
print('法1：',value)


#法2：直接计算
#运算符的优先级；括号作用；确定完成各运算的时机；做某个运算，找到正确的运算对象
#定义生成器
def tokens(text):
    text = text.split()
    for i in text:
        yield i
# 定义优先级和运算符集合
priority = {'(': 1, '+': 3, '-': 3, '*': 5, '/': 5}  # 定义优先级
infix_operators = '+-*/()'  # 定义运算符集合
def infix_exp_evaluator(line):
    st = sstack()
    exp = []
    # 对x的情况分析：
    # 1、是数字；2、是左括号；3、是右括号；4、是运算符
    # 数字就直接存入表中，左右括号决定着几个运算符的连续压人表中，
    # 栈顶的运算符需要和后的一个运算符比较后，当比后一个运算符优先级高才能入表
    for x in tokens(line):  # tokens 是一个带定义的生成器
        if x not in infix_operators:
            exp.append(float(x))
        elif st.is_empty() or x == '(':  # 左括号进栈
            st.push(x)
        elif x == ')':  # 处理右括号分支
            while not st.is_empty() and st.top() != '(':
                a = exp.pop()
                b = exp.pop()
                operator = st.pop()
                c = caculate(b,a,operator)
                exp.append(c)
            if st.is_empty():  # 没找到左括号，就不匹配
                raise SyntaxError("Missing '('.")
            st.pop()  # 弹出左括号，右括号也不进栈
        else:
            while (not st.is_empty() and priority[st.top()] >= priority[x]):
                a = exp.pop()
                b = exp.pop()
                operator = st.pop()
                c = caculate(b,a,operator) # 栈顶的运算符需要和后的一个运算符比较后，当比后一个运算符优先级高才能入表
                exp.append(c)
            st.push(x)

    while not st.is_empty():
        if st.top() == '(':
            raise SyntaxError("Extra '('.")
        a = exp.pop()
        b = exp.pop()
        operator = st.pop()
        c = caculate(b,a,operator)
        exp.append(c)
    return exp.pop()
def caculate(b,a,operator):
    if operator == '+':
        c = b + a
    elif operator == '-':
        c = b - a
    elif operator == '*':
        c = b * a
    elif operator == '/':
        if a == 0:
            raise zeroDivisionError(str(b) + '/' + str(a))
        c = b / a
    else:
        raise Exception(str(b) + operator + str(a))
    return c
# 测试
line = '( ( 1 + 2 ) * ( 3 + 4 ) - 27 ) / ( 2 + 1 )'
value = infix_exp_evaluator(line)
print('法2：', value)