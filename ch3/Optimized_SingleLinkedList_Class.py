# 改进的单链表
# 定义异常
class LListTypeError(TypeError):
    pass


class LListValueError(ValueError):
    pass


# 1、定义表节点类
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


# 定义线性链表
class LList:
    def __init__(self):
        self._head = None
        self._length = 0

    # 检测
    def is_empty(self):
        return self._head is None

    # 获取大小
    def getlen(self):
        return self._length

    def __len__(self):
        return self._length

    # 遍历
    def printall(self):
        if self._head is None:
            return -1
        else:
            point = self._head  # 临时节点
            while (point):
                print(point.elem, end='\n' if point.next_ is None else ' ')
                point = point.next_

    # 插入
    def prepend(self, elem):
        node = LNode(elem)
        if self._head is None:
            self._head = node
            self._length += 1
        else:
            node.next_ = self._head
            self._head = node
            self._length += 1

    def append(self, elem):
        node = LNode(elem)  # 新节点
        if self._head is None:
            self._head = node
            self._length += 1
        else:
            point = self._head  # 临时节点
            while (point.next_):
                point = point.next_
            point.next_ = node
            self._length += 1

    def insert(self, elem, index):
        n = self._length
        if index < 0 or index > n or self._head is None:
            raise IndexError('insert out of the range!')  # 检查范围
        if index == 0:
            self.prepend(elem)
        elif index == n:
            self.append(elem)
        else:
            i = 0
            node = LNode(elem)
            point = self._head
            while (point.next_ and i < index - 1):
                point = point.next_
                i += 1
            node.next_ = point.next_
            point.next_ = node
            self._length += 1

    # 删除
    def del_first(self):
        if self._head is None:
            raise IndexError('the List is empty!')
        elif self._length == 1:
            self._head = None
            self._length -= 1
        else:
            self._head = self._head.next_
            self._length -= 1

    def del_last(self):
        if self._head is None:
            raise IndexError('the list is empty!')
        elif self._length == 1:
            self._head = None
            self._length -= 1
        else:
            point = self._head
            while (point.next_.next_):
                point = point.next_
            point.next_ = None
            self._length -= 1

    def del_index(self, index):
        n = self._length - 1
        if index < 0 or index > n or self._head is None:
            raise IndexError('del out of the range!')  # 检查范围
        if index == 0:
            self.del_first()
        elif index == n:
            self.del_last()
        else:
            point = self._head
            i = 0
            while (point.next_ and i < index):
                point = point.next_
                i += 1
            point.next_ = point.next_.next_
            self._length -= 1

    # 比较
    def __eq__(self, another):
        if not isinstance(another, LList):
            raise LListTypeError('LListTypeError')
        self_p = self._head
        another_p = another
        while (self_p and another_p):

    # 移动链表中的元素来实现插入排序
    # 有两个循环：第一个是要插入的元素的循环；第二个是插入元素与其之前元素比较的循环；
    # 从第一个元素开始，找到比插入元素大的元素，就交换，（然后将原始插入元素之前到新插入元素位置之间的元素想右移动）
    # 交换后的元素当做插入元素，继续和剩下的原始插入元素前的元素比较交换；
    def sort1(self):
        if self._head is None:
            raise IndexError('out the range!')
        crt = self._head
        while (crt):
            x = crt.elem
            point = self._head
            while point is not crt and point.elem <= x:
                point = point.next_
            while point is not crt:
                y = point.elem
                point.elem = x
                x = y
                point = point.next_
            crt.elem = x
            crt = crt.next_

    # 通过变换链接的方式来实现插入排序
    # 同样是两个循环：第一个循环是要插入元素的循环吗；第二个循环是插入元素与其之前元素的比较循环；
    # 第二个循环的实现方式:首先将插入元素的赋给一个临时节点，并将其前一个节点的next指向其后一个节点；然后从头节点开始一直找到比插入元素
    # 大的节点的前一个节点；然后将临时节点插入到该节点之后；
    def sort(self):
        if self._head is None:
            raise IndexError('the Llist is empty!')
        if self._length == 1:
            return
        point = self._head
        rem = point.next_
        point.next_ = None
        while rem is not None:
            point = self._head
            q = None
            while point is not None and point.elem <= rem.elem:
                q = point
                point = point.next_
            if q is None:
                self._head = rem
            else:
                q.next_ = rem
            q = rem
            rem = rem.next_
            q.next_ = point
        # 测试

'''
L = LList()
L.append(1)
L.append(9)
L.prepend(7)
L.append(6)
L.printall()
print(L.getlen())
L.insert(10, 4)
L.printall()
L.sort()
L.printall()
print(L.getlen())
L.del_index(4)
L.printall()
print(L.getlen())
'''