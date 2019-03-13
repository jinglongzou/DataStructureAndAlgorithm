#######################################################################
# 表达式的计算变换过程：这里假定输入表达式是字符串，项之间是空格
#######################################################################
# 输入：字符串，项之间是空格
# 输出：计算结果
#######################################################################

# 定义一个新的栈类来存储计算过程的临时数据
# 不足两个元素时计算失败，当栈中只有一个元素时结束计算。
class esstack(sstack):
    def depth(self):
        return len(self._elems)


# 将字符行分隔为项的表
def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())


def suf_exp_evaluator(exp):  # exp是一个列表
    operators = '+-**/'
    st = esstack()
    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue
        if st.depth() < 2:
            raise SyntaxError('short of operand(s).')
        a = st.pop()
        b = st.pop()

        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '**':
            c = b ** a
        elif x == '/':
            if a == 0:
                raise zeroDivisionError(str(b) + '/' + str(a))
            c = b / a
        else:
            break
        st.push(c)
    if st.depth() == 1:
        return st.pop()
    raise SyntaxError('Extra operand(s).')


# 使用suffix_exp_evaluator(line)完成 计算
'''
# 定义一个交互式的驱动函数
def suffix_exp_caculator():
    while True:
        try:
            line = input('Suffix Expression: ')  # 有输入，所以是交互式的
            #line = '1 2 + 3 4 + * 27 - 2 1 + /'
            if line == 'end': return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print('Error: ', type(ex), ex.args)
'''
'''
#测试
line = '1 2 + 3 4 + * 27 - 2 1 + /'
suffix_exp_evaluator(line)
'''