# 所有的运算形式，加减乘除，指数，负指数 **,
#####################################################
# 中缀表达式转化为后缀表达式
####################################################
'''
#定义生成器
def tokens(text):
    text = text.split()
    for i in text:
        yield i.strip()

##########################################
'''
#########################################################
#改进tokens
##测试
#   text = '12 + 2**3- 23-4*1e-1 + 2'
#   text = '( ( 1 + 2 ) * ( 3 + 4 ) - 27 + 2**3) / ( 2 + 1 )'
#   for i in tokens(text):
#       print(i, end = ',')
########################################################
def tokens(text):
    delimiter = '/+*-()'
    i,text_len = 0,len(text)
    while(i < text_len):
        while i < text_len and text[i].isspace():
            i +=1
        if i >=text_len:
            break
        if text[i] in delimiter:
            if text[i] == '*' and text[i+1] == '*':
                yield text[i:i+2]
                i = i + 2
                continue
            yield text[i]
            i +=1
            continue
        j = i + 1
        while(j < text_len and not text[j].isspace() and text[j] not in delimiter):
            if ((text[j]=='e' or text[j] == 'E') and j + 1 < text_len and text[j + 1] == '-'):
                j +=1
            j +=1
        yield text[i:j]
        i = j
##########################################
# 定义优先级和运算符集合
priority = {'(': 1, '+': 3, '-': 3, '*': 5, '/': 5,'**':7}  # 定义优先级
infix_operators = '+-**/()'  # 定义运算符集合
# 中缀表达式转化为后缀表达式转换函数
def trans_infix_suffix(line):
    st = sstack()
    exp = []
    # 对x的情况分析：
    # 1、是数字；2、是左括号；3、是右括号；4、是运算符
    # 数字就直接存入表中，左右括号决定着几个运算符的连续压人表中，
    # 栈顶的运算符需要和后的一个运算符比较后，当比后一个运算符优先级高才能入表
    for x in tokens(line):  # tokens 是一个带定义的生成器
        if x not in infix_operators:
            exp.append(x)
        elif st.is_empty() or x == '(':  # 左括号进栈
            st.push(x)
        elif x == ')':  # 处理右括号分支
            while not st.is_empty() and st.top() != '(':
                exp.append(st.pop())
            if st.is_empty():  # 没找到左括号，就不匹配
                raise SyntaxError("Missing '('.")
            st.pop()  # 弹出左括号，右括号也不进栈
        else:
            while (not st.is_empty() and priority[st.top()] >= priority[x]):
                exp.append(st.pop())  # 栈顶的运算符需要和后的一个运算符比较后，当比后一个运算符优先级高才能入表
            st.push(x)

    while not st.is_empty():
        if st.top() == '(':
            raise SyntaxError("Extra '('.")
        exp.append(st.pop())
    return exp

'''
# 测试函数
def test_trans_infix_suffix(text):
    print('中缀表达式：',text)
    print('后缀表达式：',trans_infix_suffix(text))
    print('value: ', suf_exp_evaluator(trans_infix_suffix(text)))

#测试
text = '( ( 1 + 2 ) * ( 3 + 4 ) - 27 + 2**3) / ( 2 + 1 )'
#text = '( 1 + 2 ) * ( 3 + 4 ) - 27'
test_trans_infix_suffix(text)
'''