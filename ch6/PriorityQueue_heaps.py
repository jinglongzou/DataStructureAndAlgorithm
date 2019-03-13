#堆通过顺序表形式的完全二叉树来实现
class PrioQueueError:
    pass
class PrioQueue:
    """
    implementing priority queues using heaps
    """
    def __init__(self,elist = []):
        self._elems = list(elist)
        if elist:
            self.buildheaps()
    def is_empty(self):
        return not self._elems
    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek')
        return self._elems[0]
    def enqueue(self,e):
        self._elems.append(None)
        self.siftup(e,len(self._elems) - 1)
    def siftup(self,e,last):
        elems, i, j = self._elems,last,(last-1)//2
        while(i > 0 and e < elems[j]):
            elems[i] = elems[j]
            i,j = j,(j-1)//2
        elems[i] = e
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in peek')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e,0,len(elems))
        return e0
    def siftdown(self,e,begin,end):
        elems,i,j = self._elems,begin,2*begin + 1
        while(j < end):
            if j + 1 < end and elems[j+1] < elems[j]:
                j = j + 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i,j = j,2*j+1
        elems[i] = e
    def buildheaps(self):
        end = len(self._elems)
        for i in range(end//2,-1,-1):
            self.siftdown(self._elems[i],i,end)

'''            
 #测试
a = PrioQueue([2,1,4,7,5,3])
while not a.is_empty():
    print(a.dequeue())
'''