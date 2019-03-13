#创建一个堆结构，能够辅助图的Prim算法实现O(logV)的时间和空间复杂度
#要求：O(n)时间建堆，O(logn)的时间取最小元操作
#      从某种index出发的O(1)取出操作，即能够通过索引取出index对应的值
#      从新的index和值出发，修改、添加index和值，能够在O(logn)的时间里实现

#分析：就是实现一个小顶堆堆，其元素的(weight,起点,终点)
#      要能弹出堆顶元素，并维护堆:O(logN)
#      要能访问堆顶元素
#      要能修改堆顶元素:O(logN)
#####################################################################################
#这里基于完全二叉树来创建堆
class DecprioHeapError(Exception):
    pass
class DecPrioHeap:
    #创建
    def __init__(self,slist = []):
        self._edges = list(slist)
        self._elems = [i for i in range(len(self._edges))]
        if slist:
            self.buildheaps()

    #检查
    def is_empty(self):
        return self._elems == []
    #弹出堆顶元素，并维护堆，弹出后，向下筛选
    def dequeue(self):
        if self.is_empty():
            raise DecprioHeapError('the DecPrioHeap is empty!')
        e0 = self._elems[0]
        e = self._elems.pop()
        if len(self._elems) > 0:
            self.siftdown(e,0,len(self._elems))
        return self._edges[e0]
    #访问特定索引元素的权
    def weight(self,index):
        return self._edges[index][0]
    #修改特定索引元素
    def dec_weight(self,w,u,v):
        self._edges[v] = [w,u,v]  #修改了到顶点v的前一个顶点和权，问题是现在顶点v的索引在self._elems中不知道到了，
                                  # 就没法使用siftup来维护修改后的堆
        #寻找顶点v在elems中的索引  #这一步让修改的复杂度变成了O(V)
        end = len(self._elems)
        for i in range(len(self._elems)):
            if self._elems[i] == v:
                end = i
                break
        self.siftup(v,end)
    #向上筛选
    def siftup(self,e,last):
        edges = self._edges
        elems, i, j = self._elems,last,(last-1)//2
        while(i > 0 and edges[e][0] < edges[elems[j]][0]):
            elems[i] = elems[j]
            i,j = j,(j-1)//2
        elems[i] = e
    #向下筛选
    def siftdown(self,e,begin,end):
        edges = self._edges
        elems,i,j = self._elems,begin,2*begin + 1
        while(j < end):
            if j + 1 < end and edges[elems[j+1]][0] < edges[elems[j]][0]:
                j = j + 1
            if edges[e][0]< edges[elems[j]][0]:
                break
            elems[i] = elems[j]
            i,j = j,2*j+1
        elems[i] = e
    #键堆
    def buildheaps(self):
        end = len(self._elems)
        for i in range(end//2,-1,-1):
            self.siftdown(self._elems[i],i,end)
