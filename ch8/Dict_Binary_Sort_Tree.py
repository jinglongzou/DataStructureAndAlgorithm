###########################################################################
"""
二叉排序树：是一种存储数据的二叉树，把字典的数据存储和查询融合在二叉树的结构里
备注：采用二叉树作为字典存储结构，可以得到较高的检索效率；采用链接是的实现方式，数据项的插入删除都比较灵活方便；
二叉排序树实现字典的基本思想是：
    在二叉树的节点存储字典信息
    为二叉树安排好一种字典数据项的存储方式，利用二叉树的平均高度，可以获得较高的检索效率
因此二叉树可以实现字典关键码的有序排列；

二叉排序树或者为空或者有如下性质：
    根节点存储一个数据项
    若左子树不空，则左子树所以节点都不大于根节点
    若右子树不空，则右子树所有节点都不小于根节点
    非空的左子树、右子树都是排序二叉树

二叉排序树实现的字典性质：当且仅当中序遍历时得到的关键码是一个递增序列。

首先考虑二叉排序树的实现：
    为了支持树结构的动态变化，最常采用链接结构，因此使用BinTNode类实现二叉排序树
    在研究二叉排序树的完整类之前，首先考虑二叉排序树的检索算法
def bt_search(btree,key):
    bt = btree
    while bt is not None:
        entry = bt.data
        if key < entry.key:
            bt = bt.left
        elif key > entry.key:
            bt = bt.left
        else:
            return entry.value
    return None
"""

#首先创建二叉树的节点类
class BinTNode:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
#然后创建字典数据的结构类
class DictNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value

#二叉排序树（字典）类
#主要方法：创建、检查、查找，插入，删除，输出所有值，输出所有键值对

from Stack_chain import lstack
class DictBinTree:
    def __init__(self):
        self._root = None
    #检测
    def is_empty(self):
        return self._root is None
    #检索
    def search(self,key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if entry.key < key:
                bt = bt.left
            elif entry.key > key:
                bt = bt.right
            else:
                return entry.value
        return None
    def insert(self,key,value):
        data = DictNode(key,value) #字典数据
        node = BinTNode(data) #二叉排序树的节点
        #从根节点开始比较找新插入数据的位置
        if self._root is None:
            self._root = node
            return
        bt = self._root
        while bt is not None:
            entry = bt.data
            if entry.key > key:
                if bt.left is None:
                    bt.left = node
                    return
                bt = bt.left
            elif entry.key < key:
                if bt.right is None:
                    bt.right = node
                    return
                bt = bt.right
            else:
                bt.data.value = value #这里为什么要用bt.data,而不用entry？
                return
     #删除:保证被删除的数据项被实际删除，有保证其他数据项正常查询和使用；即删除后，排序二叉树仍是排序二叉树
    def delete(self,key):
        #首先找到对应的key
        #找到key之后要将该节点分为两种情况
        #   1、key为叶结点，则直接置其父节点的对应子节点为None
        #   2、key不位叶结点，则进一步又可分为两类
        #       ①它没有左子树，则直接将其右子树的根节点赋给其父节点的对应节点
        #       ②有左子树，则首先找到其左子树的最右叶结点，将其右子树赋给其最右叶结点的右子节点
        #          并将其左子树的根节点赋给其父节点的对应节点
        bt = self._root
        pre = None
        while bt is not None:
            entry = bt.data
            if entry.key < key:
                pre = bt
                bt = bt.left
            elif entry.key > key:
                pre = bt
                bt = bt.right
            else: #找到key所在的节点
                if bt.left is None: #key的左子树不存在
                    if pre is None: #根节点为key
                        self._root = bt.right
                        return bt.data.key,bt.data.value
                    # 根节点不为key
                    elif bt is pre.left:
                        pre.left = bt.right
                        return bt.data.key,bt.data.value
                    else:
                        pre.right = bt.right
                        return bt.data.key,bt.data.value
                else:# key的左子树存在
                    #将bt的右子树放到bt左子树的最右的叶结点
                    temp = bt.left
                    while temp.right is not None:
                        temp = temp.right
                    temp.right = bt.right
                    if pre is None:#根节点为key
                        self._root = bt.left
                        return bt.data.key,bt.data.value
                        # 根节点不为key
                    elif bt is pre.left:
                        pre.left = bt.left
                        return bt.data.key,bt.data.value
                    else:
                        pre.right = bt.left
                        return bt.data.key,bt.data.value
        return 'there is No such key!'


    #返回所有键值
    def value(self):
        #通过中序遍历可以实现键大小递增序列下的值输出
        bt = self._root
        if bt is None:
            return 'the dict is empty!'
        s = lstack()
        while bt is not None or not s.is_empty():
            while bt is not None:
                s.push(bt)
                bt = bt.left
            bt = s.pop()
            entry = bt.data
            bt = bt.right
            yield entry.value
        return 'the dict has output all values!'
    #返回所有键值对
    def entries(self):
        #通过中序遍历可以实现键大小递增序列下的值输出
        bt = self._root
        if bt is None:
            return 'the dict is empty!'
        s = lstack()
        while bt or not s.is_empty():
            while bt:
                s.push(bt)
                bt = bt.left
            bt = s.pop()
            entry = bt.data
            bt = bt.right
            yield entry.key,entry.value
        return 'the dict has output all key-values!'
# 分析：
#时间复杂度：
#   主要为查找、插入、删除三个操作，插入和删除都需要先查找，
#   插入操作在找到后，常量操作完成；删除在找到后，还好再一次查找，但是继续想叶结点查找，因此总的查找不超过树的高度
#   因此最大的复杂度为树的高度；
#   当树比较平衡时，高度为log(n),复杂度为O(log(n))；当不平衡时，最差高度为n，因此最差复杂度为O(log(n))

#空间复杂度：
#   空间复杂度只需要一个辅助空间，因此对查找、删除、插入的空间复杂度是O(1)
#   对生成器，由于使用了栈，最多也就是存储n个元素，因此空间复杂度最差是O(n)
#测试
dicts = DictBinTree()
dicts.insert(3,4)
dicts.insert(1,2)
dicts.insert(7,9)
dicts.insert(4,5)

print('\n')
for value in dicts.value():
    print(value)
print('\n')
print(list(dicts.delete(3)))
print('\n')
for value in dicts.entries():
    print(list(value))