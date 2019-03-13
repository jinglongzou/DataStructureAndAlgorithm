# 队列
class Node:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


class lqueue:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def top(self):
        if self._rear is None:
            raise queueUnderflow('in stack top!')
        return self._rear.next_.elem

    def inqueue(self, elem):
        node = Node(elem)
        if self._rear is None:
            node.next_ = node
            self._rear = node
        node.next_ = self._rear.next_
        self._rear.next_ = node
        self._rear = node

    def dequeue(self):
        if self._rear is None:
            raise queueUnderflow('in stack top!')
        point = self._rear.next_
        if point is self._rear:
            self._rear = None  # 最后一个弹出后需要置为None
            return point.elem
        else:
            self._rear.next_ = point.next_
            return point.elem

'''
# 测试
queue = lqueue()
for i in range(3):
    queue.inqueue(i)
try:
    while (queue):
        print(queue.dequeue(), end=' ')
except queueUnderflow as e:
    print('\nqueue has exported all elems!')
'''