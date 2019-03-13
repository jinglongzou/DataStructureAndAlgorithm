###############################################################
# 循环链表功能介绍                                            #
###############################################################
#1、创建
#2、检测
#3、长度
#4、插入：前端，后端、任意位置
#5、删除：基于元素，基于位置
#############################################################
#循环链表为了方便前端、后端插入，使用尾指针，而不使用头指针
############################################################
#定义两种异常
class ClistTypeError(TypeError):
    pass
class ClistValueError(ValueError):
    pass
#定义节点
class Node:
    def __init__(self,elem,next_ = None):
        self.elem = elem
        self.next_ =next_
#定义表
class Clist:
    #创建
    def __init__(self):
        self.rear_ = None
    #判断
    def is_empty(self):
        return self.rear_ is None
    def length(self):
        count = 0
        if self.rear_ is None:
            return count
        else:
            point = self.rear_.next_
            while(point is not self.rear_):
                count +=1
                point = point.next_
            return count + 1
    #输出
    def printC(self):
        if self.rear_ is None:
            return
        else:
            point = self.rear_.next_
            while point is not self.rear_:
                print(point.elem,end = ' ')
                point = point.next_
            print(point.elem)
    #插入
        #前端
    def prepend(self,elem):
        node = Node(elem)
        if self.rear_ is None:
            node.next_ = node
            self.rear_ = node
        else:
            node.next_ = self.rear_.next_
            self.rear_.next_ = node
        #后端
    def append(self,elem):
        node = Node(elem)
        if self.rear_ is None:
            node.next_ = node
            self.rear_ = node
        else:
            node.next_ = self.rear_.next_
            self.rear_.next_ = node
            self.rear_ = node
        #任意
    def insert_index(self,elem,index):
        n = self.length()
        if index < 0 or index > n:
            raise IndexError('out the range of the Clist! ')
        if index == 0:
            self.prepend(elem)
        elif index == n:
            self.append(elem)
        else:
            i = 0
            node = Node(elem)
            point = self.rear_.next_
            while(point.next_ is not self.rear_ and i < index):
                point = point.next_
            node.next_ = point.next_
            point.next_ = node
    #删除
        #前端
    def delete_first(self):
        if self.rear_ is None:
            raise LinkedListUnderflow('in delete of Clist')
        point = self.rear_.next_
        if self.rear_ is point:
            self.rear_ = None
        else:
            self.rear_.next_ = point.next_ #point 即为头节点
        return point.elem
        #尾端
    def delete_last(self):
        if self.rear_ is None:
            raise LinkedListUnderflow('in delete of Clist')
        point = self.rear_.next_
        if self.rear_ is point:
            self.rear_ = None
        else:
            while(point.next_ is not self.rear_):
                point = point.next_
            self.rear_ = point #point.next_即为尾节点
        return point.next_.elem
        #基于元素
    def delete_elem(self,elem):
        if self.rear_ is None:
            ClistValueError('no such elem!')
        else:
            point = self.rear_.next_
            prev = self.rear_
            while(point is not self.rear_ and point.elem != elem):
                prev = point
                point = point.next_
            if point.elem == elem:
                if prev is self.rear_ and point is self.rear_ and point.elem == elem: #只有一个节点
                    self.rear_ = None
                elif prev is self.rear_ : #elem是首节点
                    self.delete_first()
                elif point is self.rear_ and point.elem == elem: #elem是尾节点
                    prev.next_ = point.next_
                    self.rear_ = prev
                else: #中间任意节点
                    prev.next_ = point.next_
                return elem
            else:
                raise ClistValueError('no such elem!')
        #基于索引
    def delete_index(self,index):
        n = self.length()
        if index < 0 or index > n - 1 or self.rear_ is None:
            raise IndexError('out the range of the Clist! ')
        point = self.rear_.next_
        prev = self.rear_
        i = 0
        while(point is not self.rear_ and i < index):
            prev = point
            point = point.next_
            i +=1
        if i == index:
            if prev is self.rear_ and point is self.rear_: #只有一个元素
                self.rear_ = None
            elif prev is self.rear_: #首节点
                self.delete_first()
            elif point is self.rear_: #尾节点
                prev.next_ = point.next_
                self.rear_ = prev
            else:                     #中间节点
                prev.next_ = point.next_
        else:
            raise ClistValueError('no such elem!')
'''
#测试
CL = Clist()
for i in range(3):
    CL.append(i)
#输出
CL.printC()
#插入
CL.insert_index(10,3)
#删除
CL.delete_index(2)
#输出
CL.printC()
#大小
CL.length()
'''
