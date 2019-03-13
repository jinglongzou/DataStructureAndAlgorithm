# 定义栈的异常
class stackUnderflow(ValueError):
    pass
# 栈的顺序表实现：
# 栈的顺序表实现：
class sstack:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise stackUnderflow('in stack top!')
        return self._elems.pop()

    def top(self):
        if self._elems == []:
            raise stackUnderflow('in stack top!')
        return self._elems[-1]

'''
# 测试
s1 = sstack()
for i in range(3):
    s1.push(i)

try:
    while (s1):
        print(s1.pop(), end=' ')
    print('\n')
except stackUnderflow as e:
    print('\nstack has exported all elems!')
'''