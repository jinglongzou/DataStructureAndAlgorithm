# 顺序存储结构的线性表实现
class List:
    # 创建
    def __init__(self, max_num=10, increment=10):
        self._max = max_num
        self._increment = increment
        self._num = 0
        self.data = [None] * self._max

    # 检测
    def is_empty(self):
        return self._num == 0

    def is_full(self):
        return self._num == self._max

    def ergodicity(self):
        for i in range(self._num):
            print(self.data[i])

    def find(self, elem):
        if self._num == 0:
            return -1  # 未找到
        else:
            index = 0
            flag = False  # 未找到
            for i in range(self._num):
                if self.data[i] == elem:
                    index = i
                    return index
            if not flag:
                return -1  # 未找到

    def find_after_d(self, d, k):
        if self._num <= d:
            return -1  # 未找到
        else:
            index = d
            flag = False  # 未找到
            for i in range(d, self._num):
                if self.data[i] == elem:
                    index = i
                    return index
            if not flag:
                return -1  # 未找到

    # 大小
    def len(self):
        return self._num

    # 插入
    def prepend(self, elem):
        for i in range(self._num, 0, -1):
            self.data[i] = self.data[i - 1]
        self.data[0] = elem
        self._num += 1

    def append(self, elem):
        if self._num < self._max:
            self.data[self._num] = elem
            self._num += 1
        else:
            raise IndexError('append IndexError')

    def insert(self, elem, i):
        if self._num < self._max:
            for k in range(self._num, i, -1):
                self.data[i] = self.data[i - 1]
            self.data[i] = elem
            self._num += 1
        else:
            raise IndexError('insert IndexError')

    def __setitem__(self, elem, i):
        if not isinstance(i, int):
            raise TypeError
        if i < self._num and i >= 0:
            self.data[i] = elem
        else:
            raise IndexError('setitem IndexError')

    # 删除
    def del_first(self):
        if self._num > 0:
            for i in range(self._num - 1):
                self.data[i] = self.data[i + 1]
            self.data[self._num - 1] = None
            self._num -= 1
        else:
            raise IndexError('the List is empty!')

    def del_last(self):
        pass

    def del_i(self, i):
        pass

    # 搜索
    def __getitem__(self, i):
        if not isinstance(i, int):
            raise TypeError
        if i < self._num and i >= 0:
            return self.data[i]
        else:
            raise IndexError('getitem IndexError')

    def forall(self):
        pass

