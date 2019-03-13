##############################################################################
'''
ADT Dict:
    Dict(self):
    is_empty(sefl):
    num(self):
    search(self,key):
    insert(self,key,value):
    delete(self,key):
    value(self):   #迭代的方式获取值
    entries(self):  #迭代的方式获取逐对的键和值
'''
#字典线性表的实现
#通过tuple或者list的二元组来存储键和值
#字典以线性表的形式存储。那么键是否有序就决定了插入、删除操作与查找操作的效率了
#这里按键的大小从小到大存储，因此插入和删除的复杂度我O(n)，查找的复杂度通过二分法可以降到log(n)
#异常
class DictListError(Exception):
    pass
class DictList:
    def __init__(self):
        self._elems = []
    def is_empty(self):
        return not self._elems
    def num(self):
        return len(self._elems)
    def search(self,key):
        elems = self._elems
        n = len(self._elems)
        begin = 0
        last = n - 1
        while begin <= last:
            mid = (last - begin) // 2 + begin
            if elems[mid][0] >key:
                last = mid - 1
            elif elems[mid][0] < key:
                begin = mid + 1
            else:
                return elems[mid]
    def insert(self,key,value):
        elems = self._elems
        n = len(self._elems)
        if n == 0:
            elems.append((key,value))
            return
        begin = 0
        last = n - 1
        while(begin < last):
            mid = (last - begin) // 2 + begin
            if elems[mid][0] < key:
                begin = mid + 1
            elif elems[mid][0] > key:
                last = mid -1
            else:
                elems[mid] = (key,value)
                return
        if elems[begin][0] > key:  #key小，所以就插入begin位置
            elems.insert(begin,(key,value))
            return
        else:                      #key大，所以就插入begin后的一个位置
            elems.insert(begin+1,(key,value))
            return
    def delete(self,key):
        if self.is_empty():
            raise DictListError('the dict is empty!')
        elems = self._elems
        n = len(self._elems)
        begin = 0
        last = n - 1
        while(begin < last):
            mid = (last - begin) // 2 + begin
            if elems[mid][0] < key:
                begin = mid + 1
            elif elems[mid][0] > key:
                last = mid -1
            else:
                e = elems[mid]
                for i in range(mid,n-1):
                    elems[i] = elems[i+1]
                elems.pop(-1)
                return e
        raise DictListError('there is no such {} in dict!'.format(key))
    def value(self):
        if self.is_empty():
            return None
        n = len(self._elems)
        for i in range(n):
            yield self._elems[i][1]
    def entries(self):
        if self.is_empty():
            return None
        n = len(self._elems)
        for i in range(n):
            yield self._elems[i]



#测试
dicts = DictList()
dicts.insert(1,2)
dicts.insert(3,4)
dicts.insert(7,9)
dicts.insert(4,2)
for value in dicts.entries():
    print(value)
print(dicts.delete(3))
print('\n')
for value in dicts.entries():
    print(value)