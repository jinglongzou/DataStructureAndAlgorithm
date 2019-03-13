# 基于list的方法
def josephus_A(n, k, m):
    people = list(range(1, n + 1))

    i = k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end='')
                people[i] = 0
            i = (i + 1) % n  # i是循环索引
        if num < n - 1:
            print(', ', end='')
        else:
            print(' ')
    return


# 基于顺序表的方法，每退出一个人就删除一个元素；

def josephus_B(n, k, m):
    people = list(range(1, n + 1))

    num, i = n, k - 1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i), end=(', ' if num > 1 else '\n'))
    return


# 基于循环表的方法
class josephus_C(Clist):
    def turn(self, m):
        for i in range(m):
            self.rear_ = self.rear_.next_

    def __init__(self, n, k, m):
        # 构建循环链表
        Clist.__init__(self)
        for i in range(1, n + 1):
            self.append(i)
        # 存储开始计数位置k和第几个人退出m
        self.start = k
        self.increment = m

    def compute(self):
        self.turn(self.start - 1)
        while not self.is_empty():
            self.turn(self.increment - 1)
            print(self.delete_first(), end='\n' if self.is_empty() else ', ')

'''
josephus_A(10, 2, 7)
josephus_B(10, 2, 7)
s = josephus_C(10, 2, 7)
s.compute()
'''