# 定义栈的异常
class stackUnderflow(ValueError):
    pass
# 栈的顺序表实现：
class sstack:
    def __init__(self,init_len = 8):
        self._len = init_len
        self._elems = [0] * self._len
        self._num = 0

    def is_empty(self):
        return self._num ==0

    def push(self, elem):
        if self._num == self._len:
            self.__extend
        self._elems.append(elem)
        self._num +=1

    def pop(self):
        if self._elems == [] or self._num == 0:
            raise stackUnderflow('in stack top!')
        self._num -=1
        return self._elems.pop()

    def top(self):
        if self._elems == []:
            raise stackUnderflow('in stack top!')
        return self._elems[-1]
    def __extend(self):
        old_len = self._len
        self._len *=2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[i]
        self._elems = new_elems

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
