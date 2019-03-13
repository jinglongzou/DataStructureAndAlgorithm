# 链表实现
class Node:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


class lstack:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def top(self):
        if self._head is None:
            raise stackUnderflow('in stack top!')
        point = self._head
        self._head = self._head.next_
        return self._head.elem

    def push(self, elem):
        node = Node(elem)
        if self._head is None:
            self._head = node
        else:
            node.next_ = self._head
            self._head = node

    def pop(self):
        if self._head is None:
            raise stackUnderflow('in stack top!')
        point = self._head
        self._head = point.next_
        return point.elem

'''
# 测试
s2 = lstack()
for i in range(3):
    s2.push(i)
try:
    while (s2):
        print(s2.pop(), end=' ')
    print('\n')
except stackUnderflow as e:
    print('\nstack has exported all elems!')
'''