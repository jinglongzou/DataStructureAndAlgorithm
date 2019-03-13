###############################################################
# 单链表功能介绍
# 1、创建
# 2、检测
# 3、长度
# 4、插入：前端，后端、任意位置
# 5、删除：基于元素，基于位置
#############################################################
# 单链表
# 定义异常
class LlistTypeError(TypeError):
    pass


class LlistValueError(ValueError):
    pass


# 定义节点
class Node:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


class Llist:
    # 创建
    def __init__(self):
        self.head_ = None

    # 检查
    def is_empty(self):
        return self.head_ is None

    # 长度
    def length(self):
        count = 0
        if self.head_ is None:
            return count
        else:
            point = self.head_
            while (point):
                count += 1
                point = point.next_
            return count

    # 插入
    # 末尾插入
    def append(self, elem):
        node = Node(elem)
        if self.head_ is None:
            self.head_ = node
        else:
            point = self.head_
            while (point.next_):
                point = point.next_
            point.next_ = node
        # 前端插入

    def prepend(self, elem):
        node = Node(elem)
        if self.head_ is None:
            self.head_ = node
        else:
            node.next_ = self.head_
            self.head_ = node
        # 任意位置插入

    def insert_index(self, elem, index):
        n = self.length()
        if index < 0 or index > n:
            raise IndexError
        length = self.length()
        if index == 0:
            self.prepend(elem)
        elif index == length:
            self.append(elem)
        else:
            node = Node(elem)
            point = self.head_
            i = 0
            while (point.next_ and i < index - 1):
                point = point.next_
                i += 1
            node.next_ = point.next_
            point.next_ = node

    # 删除
    # 基于元素的删除
    def delete_elem(self, elem):
        if self.head_ is None:
            raise LlistValueError('the Clist is empty!')
        else:
            point = self.head_
            prev = None
            while (point and point.elem != elem):
                prev = point
                point = point.next_
            if prev == None:
                self.head_ = self.head_.next_  # 第一个元素即为所找
            elif point:
                prev.next_ = point.next_  # 找到的元素
            else:
                return 'no such elem'  # 不存在该元素
        # 基于位置删除 ，基于索引删除

    def delete_index(self, index):  # index是索引，不是位置
        if index < 0 or index > self.length() - 1:
            raise IndexError
        point = self.head_
        prev = None
        i = 0
        while (point and i < index):
            prev = point
            point = point.next_
            i += 1
        if prev is None:
            self.head_ = self.head_.next_
        elif point:
            prev.next_ = point.next_  # 找到的元素
        else:
            return 'no such elem'  # 不存在该元素

    # 输出
    def printL(self):
        if self.head_ is None:
            return
        else:
            point = self.head_
            while (point):
                print(point.elem, end=' ')
                point = point.next_

'''
# 测试
L = Llist()
L.append(1)
L.append(2)
L.append(4)
L.insert_index(3, 2)
L.printL()
L.delete_index(3)
print()
L.printL()
L.length()
'''