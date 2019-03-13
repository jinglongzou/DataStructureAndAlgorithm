#基于连续表的实现，并且采用通过位置顺序来表达优先级
class PrioQueueError:
    pass
class PrioQueue:
    def __init__(self,elist = []):
        self._elems = list(elist)
        self._elems.sort(reverse = True)
    def enqueue(self,e):
        i = len(self._elems)
        while(i >= 0 and e >= self._elems[i]):
            i -=1
        self._elems.insert(i+1,e)
    def is_empty(self):
        return not self._elems
    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in top')
        return self._elems[-1]
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in top')
        return self._elems.pop()