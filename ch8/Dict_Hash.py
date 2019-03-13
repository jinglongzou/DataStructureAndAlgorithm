#############################################################################
#基于散列表实现字典
#如何能快速找到所需的数据：如果数据项连续存储，而关键码就是存储数据的地址。
#如果关键码不能或者不合适作为数据存储的下标，可以通过一个变换把它们映射到一种下标。
# 这样吧基于关键码的检索转化为基于整数下标的直接检索。
################################################################################
#散列表的思想实现字典，具体方法：
#选定一个整数的下标范围，建立一个包括相应元素位置范围的顺序表
#选择一个从实际关键码到上述下标范围的适当映射h：
#   将关键码为key的数据，存入表h(key)个位置，查找是查找h(key)个位置的元素
##################################################################################
#散列表的关键问题：
#   散列函数选择：
#       数字分析法，折叠法，中平方法；常用散列函数：除余法，基数转换法
#   冲突解决机制：
#       内消解法：在基本存储区内部解决
#           开地址法
#           探查序列
#       外消解法：在基本存储区外部解决
#           溢出区法
#           桶散列
##########################################################################
#散列表的性质
#扩大存储区，用空间换取时间；扩大存储区后，还要调整散列函数，以便极可能的利用增加的存储单元
#扩大存储区需要付出重新分配存储区和在散列装入数据项的代价
### 随着负载因子的增大，冲突的可能性越大
"""""""散列表的负载因子对效率有决定性影响，当采用内部消融机制时，负载因子<= 0.7~0.75时，散列表的平均长度接近常数
#散列表的许多性质时概率性的
###################################################################################
#实现桶散列的字典，也就是通过链表来存储字典元素
#而每个桶的前端作为头结点，是顺序存储的，其指向一个字典元素
#首先创建字典节点：
class DictNode:
    def __init__(self,key,value):
        self.elems = [key,value]
        self.next = None
    def __lt__(self,other):
        return self._elems[0] < other.elems[0]
    def __le__(self,other):
        return self._elems[0] <= other.elems[0]
#异常
class DictHashError(Exception):
    pass
#构建桶散列的字典
class DictHash:
    def __init__(self,num = 10):
        self._heads = [None] * num
        self._num = num
        self.count = 0
    def is_empty(self):
        return  self.count == 0
    def insert(self,key,value):
        node = DictNode(key, value)
        hash_key = key % self._num
        #初始为None
        if self._heads[hash_key] is None:
            #point = node
            self._heads[hash_key] = node
            self.count +=1
            return
        # 初始不为None，按照从小到大顺序存，那么首先找到比key大的元素
        point = self._heads[hash_key]
        pre_point = None
        #找到比不小于key的元素 或者到链表的末尾了
        while not point and point.elems[0] < key:
            pre_point = point
            point = point.next
        #到链表的末尾了
        if point is None:
            point = node
            self.count += 1
        #找到不小key的元素了，相同大小的key就修改值
        elif point.elems[0] == key:
            point.elems[1] = value
        # 不同大小的key，就修改节点，也就是找到了比key大的元素
        else:
            node.next = point
            pre_point.next = node
            self.count += 1
    def delete(self,key):
        hash_key = key % self._num
        point = self._heads[hash_key]
        if point is None:
            raise DictHashError('befor cycle, not exist the key!')
        pre_point = None
        while point:
            if point.elems[0] < key:
                pre_point = point
                point = point.next
            elif point.elems[0] > key:
                raise DictHashError('in cycle,not exist the key!')
            else:
                if pre_point is None:
                    self._heads[hash_key] = point.next
                    self.count -= 1
                    return point.elems
                else:
                    pre_point.next = point.next
                    self.count -= 1
                    return point.elems
        raise DictHashError('after cycle,not exist the key!')
    #这里要输出所有的值
    def value(self):
        if self.is_empty():
            return None
        for i in range(self._num):
            if self._heads[i] is None:
                continue
            else:
                point = self._heads[i]
                while(point):
                    elem = point.elems[1]
                    point = point.next
                    yield elem


    #输出所有键值对
    def entries(self):
        if self.is_empty():
            return None
        for i in range(self._num):
            if self._heads[i] is None:
                continue
            else:
                point = self._heads[i]
                while(point):
                    elem = point.elems
                    point = point.next
                    yield elem
#测试
dicts = DictHash()
dicts.insert(1,2)
dicts.insert(3,4)
dicts.insert(7,9)
dicts.insert(4,2)
print(dicts.count)
print('\n')
for value in dicts.value():
    print(value)
print('\n')
print(dicts.delete(3))
print('\n')
for value in dicts.entries():
    print(value)

