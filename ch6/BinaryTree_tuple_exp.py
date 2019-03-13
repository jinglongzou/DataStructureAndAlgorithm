#构造表达式
def make_sum(a,b):
    return ('+',a,b)
def make_prod(a,b):
    return ('*',a,b)
def make_diff(a,b):
    return ('-',a,b)
def make_div(a,b):
    return ('/',a,b)
##测试
exp = make_prod(2,make_sum(1,3))

#在定义表达式处理函数时，需要经常判断基本表达式和复合表达式。检查a是否是一个数值
def is_basic_exp(a):
    return not isinstance(a,tuple)
#检查是否是可以计算的数值型对象
def is_number(x):
    return (isinstance(x,int) or isinstance(x,float) or isinstance(x,complex))
#表达式求值
def eval_exp(e):
    if is_basic_exp(e):
        return e
    op, a, b = e[0],eval_exp(e[1]),eval_exp(e[2])
    if op == '+':
        return eval_sum(a,b)
    elif op =='*':
        return eval_prod(a,b)
    elif op == '-':
        return eval_diff(a,b)
    elif op == '/':
        return eval_div(a,b)
    else:
        raise ValueError('Unknown operator: ',op)
#求值函数
def eval_sum(a,b):
    if is_number(a) and is_number(b):
        return a + b
    if is_number(a) and a == 0:
        return b
    if is_number(b) and b == 0:
        return a
    return make_sum(a,b)
def eval_div(a,b):
    if is_number(a) and is_number(b):
        return a/b
    if is_number(a) and a == 0:
        return 0
    if is_number(b) and b == 1:
        return a
    if is_number(b) and b == 0:
        raise ZeroDivisionError
    return make_div(a,b)
def eval_prod(a,b):
    if is_number(a) and is_number(b):
        return a * b
    if is_number(a) and a == 0:
        return 0
    if is_number(b) and b == 0:
        return 0
    if is_number(a) and a == 1:
        return b
    if is_number(b) and b == 1:
        return a
    return make_prod(a,b)
def eval_diff(a,b):
    if is_number(a) and is_number(b):
        return a - b
    if is_number(a) and a == 0:
        return b
    if is_number(b) and b == 0:
        return a
    return make_diff(a,b)
## 测试
exp = make_prod(2,make_sum(1,3))
eval_exp(exp)
