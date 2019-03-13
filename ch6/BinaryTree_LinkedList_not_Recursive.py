#单向二叉树
#首先创建节点类
class BinTNode:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
#测试
t = BinTNode(1,BinTNode(2),BinTNode(3))
#计数统计
def count_BinTNode(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNode(t.left) + count_BinTNode(t.right)
#前序遍历
def preorder(t,proc):
    if t is None:
        return
    proc(t.data)
    preorder(t.left,proc)
    preorder(t.right,proc)
#################################
#递归定义的二叉树操作具有统一的模式，包括两个部分
#   对空树的处理
#   对非空树的处理
#       如何处理根节点
#       递归调用处理左右子树
#       基于上述三个部分处理的结果得到整个树的处理结果。
################################################################################
#我创建了一个二叉树链表类，然后我要给他封装一些方法
###############################################################################

from Stack_linear import sstack,stackUnderflow
class BTree:
    #初始化
    def __init__(self,head = None):
        self._head = head
    #某操作,
    def proc(self,data):
        print(data, end = ' ')
    def get_head(self):
        return self._head
    #检查
    def is_empty(self):
        return self._head is None
    def root(self):
        return self._head.data
    def leftchild(self):
        return self._head.left
    def rightchild(self):
        return self._head.right
    def set_root(self,data):
        self._head.data = data
    def set_left(self,left):
        self._head.left = left
    def set_right(self,right):
        self._head.right = right
    def get_head(self):
        return self._head
    def set_head(self,bintreeNode):
        self._head = bintreeNode
    ##############################################################
    #非递归遍历方法
    #############################################################
    #前序遍历
    def preorder(self):
        '''
        对每个节点先处理
        然后将右节点入栈

        处理右子树
        :return:
        '''
        point = self._head
        if point is None:
            return
        s = sstack()
        while point is not None or not s.is_empty():
            while point is not None:
                self.proc(point.data)
                if point.right != None:
                    s.push(point.right)
                point = point.left
            if not s.is_empty():
                point = s.pop()


    # 中序遍历
    def midorder(self):
        '''
        先根入栈，
        然后处理左节点
        然后转向右节点
        :return:
        '''
        point = self._head
        if point is None:
            return
        s = sstack()
        while point is not None or not s.is_empty():
            while point is not None:
                s.push(point)
                point = point.left
            point = s.pop()
            self.proc(point.data)
            point = point.right

    # 后序遍历
    def postorder(self):
        point = self._head
        if point is None:
            return
        s = sstack()
        while point is not None or not s.is_empty():
            while point is not None:
                s.push(point)
                point = point.left if point.left is not None else point.right
            point = s.pop()
            self.proc(point.data)
            if not s.is_empty() and s.top().left == point:
                point = s.top().right
            else:
                point = None
    ##############################################################
    #递归遍历方法
    ##############################################################
    #先根递归遍历
    def recursive_preorder(self,tree):
        point = tree
        if point is None:
            return
        self.proc(point.data)
        self.recursive_preorder(point.left)
        self.recursive_preorder(point.right)
    #中根递归遍历
    def recursive_midorder(self,tree):
        point = tree
        if point is None:
            return
        self.recursive_midorder(point.left)
        self.proc(point.data)
        self.recursive_midorder(point.right)
    #后根递归遍历
    def recursive_postorder(self,tree):
        point = tree
        if point is None:
            return
        self.recursive_postorder(point.left)
        self.recursive_postorder(point.right)
        self.proc(point.data)


    #相等判断
    #递归的相等判断
    def __eq__(self, other):
        if not isinstance(other,BTree):
            raise TypeError('wrong type!')
        point1 = self._head
        point2 = other.get_head()
        #递归的方法
        def is_equal(point1,point2):
            if point1 is None and point2 == point2:
                return True
            #基于先根遍历
            if point1.data != point2.data:
                return False
            else:
                return True
            is_equal(point1.left,point2.left)
            is_equal(point1.right,point2.right)
        #非递归的方法
        def is_equal_Not_recursive(point1,point2):
            if point1 is None and point2 == point2: #两棵树都为None
                return True
            elif point1 is not None and point2 is not None: #两棵树都不为None
                s1 = sstack()
                s2 = sstack()
                while ((point1 is not None and point2 is not None) or (not s1.is_empty() and not s2.is_empty())):
                    if point1 is not None and point2 is not None:  # 两个节点都不是None
                        if point1.data != point2.data:
                            return False
                        s1.push(point1.right)
                        s2.push(point2.right)
                        point1 = point1.left
                        point2 = point2.left
                    elif point1 is None and point2 is None: #两个节点都是None
                        if not s1.is_empty() and not s2.is_empty(): #都不是空栈
                            point1 = s1.pop()
                            point2 = s2.pop()
                        elif s1.is_empty() and s2.is_empty(): #都是空栈
                            pass
                        else:#一个是空栈，一个不是
                            return False
                    else: #一个节点是None,一个节点不是None
                        return False
                return True
            else: #一棵树是None，一棵树不是None
                        return False
        return is_equal_Not_recursive(point1,point2)

    #克隆
    def clone(self):
        newtree = BTree()
        newtree_head = newtree.get_head()
        point = self._head
        #递归的前根遍历法
        def clone_(point):
            if point is None:
                return None
            data = point.data
            left = clone_(point.left)
            right = clone_(point.right)
            return BinTNode(data,left,right)
        newtree_head = clone_(point)
        newtree.set_head(newtree_head)
        return newtree
    #非递归方法的克隆
    def clone_not_recursive(self):
        point = self.set_head()
        if point is None:
            return None
        newtree = BTree()
        point_new = newtree.get_head()
        s1 = sstack()
        s2 = sstack()
        while point is not None or not s1.is_empty():
            while point is not None:
                node = BinTNode(point.data)
                s1.push(point.right)
                if node is None:
                    point_new = node
                    s2.push(point_new)
                else:
                    s2.top().left = node
                    s2.push(node)
                point = point.left
            point = s1.pop()
            s2.top().right = point #弹出的元素要立即赋给s2栈顶的右节点
            s2.pop()               #弹出栈顶元素
            point = point.left     #原始节点的左子树
        newtree.set_head(point_new)
        return newtree
    #########################################################################
    #小结：
    #通过非递归方法对每个节点实现操作，主要通过栈来实现，对于克隆，比较这种两个BTree对象的就需要两个栈来实现
    #基本的逻辑还是非递归遍历的思路，只是proc这个操作变化了。
    ##########################################################################################
    #节点计数
    #递归的方法
    def count_nodes(self):
        point = self._head
        num = 0
        #递归的方法
        def count_nodes_recursive(point):
            if point is None:
                return num
            left = count_nodes_recursive(point.left)
            right = count_nodes_recursive(point.right)
            return num + 1 + left + right
        return count_nodes_recursive(point)
    #非递归的方法：
    def count_nodes_not_recursive(self):
        point = self._head
        num = 0
        if point is None:
            return num
        s = sstack()
        while(point is not None or not s.is_empty()):
            while point is not None:
                num +=1
                if point.right is not None:
                    s.push(point.right)
                point = point.left
            if not s.is_empty():
                point = s.pop()
        return num

    ###################################################
    #习题小结：相等判断、克隆无法利用现有的遍历方法，但是节点计数可以利用
    ########################################################################
#测试
t = BinTNode(1,BinTNode(2,BinTNode(4)),BinTNode(3))
k = BTree(t)
k.preorder()
print('\n')
k.midorder()
print('\n')
k.postorder()
print('\n')
k.recursive_preorder(k.get_head())
print('\n')
k.recursive_midorder(k.get_head())
print('\n')
k.recursive_postorder(k.get_head())
print('\n')
g = BTree(t)
print(k == g)
print('\n')
Q = BTree()
Q = k.clone()
Q.recursive_postorder(Q.get_head())
print('\n')
P = k.clone()
P.recursive_postorder(P.get_head())
print('\n')
print(P.count_nodes())
print(P.count_nodes_not_recursive())
