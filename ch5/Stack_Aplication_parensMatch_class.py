# 栈的应用 括号的匹配 利用栈先进后出的特性来实现
# 从一个字符串中匹配出括号：首先括号集合要有；然后入栈的元素集合要有；括号匹配关系的集合要有；
# 异常
class notMatchError(Exception):
    pass
class check_parentheses:
    def __init__(self):
        self.parens = '()[]{}'
        self.open_parens = '([{'
        self.opposite = {')': '(', ']': '[', '}': '{'}
    def char_yield(self,text):
        i, text_len = 0, len(text)
        while (True):
            while i < text_len and text[i] not in self.parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
    def check_parens(self,text,line_num):
        st = sstack()  # 保存括号的栈 这里使用的顺序表形式的栈
        for pr, i in self.char_yield(text):
            if pr in self.open_parens:
                st.push(pr)
            elif st.pop() != self.opposite[pr]:
                print('Unmatching is found at the {} of line {} for {}'.format(i,line_num, pr))
                raise notMatchError

            # else: 这次匹配成功什么也不做
        print('All parentheses are correctly matched!')
        return True

'''
# 测试
check = check_parentheses()
text = 'afa(aklfa{afjha[Lalk;fka;f]alkfaf[afalla]})'
#check.check_parens(text)
# 应用——从文件读取数据，在发现不匹配时，不仅输出不匹配的括号，好输出括号所在的行号和字符位置

fr = open(r'E:\python program\Jupyter-notebook\myenv\数据结构与算法\testdata\stack_queue\parens_test.txt')
line_num = 0
check = check_parentheses()
for line in fr:
    try:
        #print(line,i)
        check.check_parens(line,line_num)
        line_num +=1
    except Exception as e:
        continue
'''