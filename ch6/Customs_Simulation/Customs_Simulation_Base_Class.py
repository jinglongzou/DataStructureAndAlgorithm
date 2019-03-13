# 首先开发一个通用的模拟框架类
# 一个模拟需要维护的属性有：事件队列，当前时间，模拟总时间
# 一个模拟需要的方法有：创建模拟器，执行事件，添加时间，返回当前时间

from random import randint
from PriorityQueue_heaps import PrioQueue
from Queue_SequenseList import squeue

class Simulation:
    def __init__(self,duration):
        self._eventq = PrioQueue()
        self._time = 0
        self._duration = duration
    def run(self):
        while not self._eventq.is_empty():
            event = self._eventq.dequeue()
            self._time = event.time()
            if self._time > self._duration:
                break
            event.run()
    def add_event(self,event):
        self._eventq.enqueue(event)
    def cur_time(self):
        return self._time

#对任何一个具体的模拟，只需要根据情况实现一组特殊的事件类。
# 为了规范所以的事件类，首先定义一个公共事件基类
#事件基类需要维护的属性：事件时间，host:表示有关事件的发生所在的模拟系统（宿主系统）
#事件所需要的方法：创建，小于比较，小于等于比较，返回宿主系统，返回事件时间，事件的执行

class Event:
    def __init__(self,event_time,host):
        self._ctime = event_time
        self._host = host
    def __lt__(self,other_event):
        return self._ctime <other_event.time()
    def __le__(self,other_event):
        return self._ctime <= other_event.time()
    def host(self):
        return self._host
    def time(self):
        return self._ctime
    def run(self):
        pass

#########################################################################
#改进的waitline
# 当前还是基于每[a, b]分钟到来一辆车
# 主要改进检查通道的等待队列，让每一个通道都有一个等待队列
# 因此对一个车辆它需要做两个判断，来决定它的下一步操作：
#   判断当前是否有空的检查通道：
#       有：就进入该通道检查
#       没有：就查找当前等待车辆最少的等待队列进入
# 因此，改进的关键在于修改等待队列，改为通道数个队列，
# 并且每个通道有一个等待车辆计数，即为通道的等待队列的权

class Waitline:
    def __init__(self, gate_num):
        self._waitline_num = gate_num
        self._weight = [0] * self._waitline_num
        self._waitline = {}
        for i in range(gate_num):
            self._waitline[i] = squeue()
    def is_empty(self):
        flag = True
        for i in range(self._waitline_num):
            if not self._waitline[i].is_empty():
                flag = False
                return flag
        return flag
    def enqueue(self, waitline_index,car):
        self._waitline[waitline_index].enqueue(car)
        self._weight[waitline_index] +=1

    def dequeue(self,gate_index):
        waitline_index = gate_index
        self._weight[waitline_index] -=1
        return self._waitline[waitline_index].dequeue()
    def get_waitline_num(self):
        return self._waitline_num
    def get_waitline_weight(self):
        return self._weight
    # 检查某等待队列里是否有车
    def has_queued_car(self, waitline_index):
        return not self._waitline[waitline_index].is_empty()

    #统计剩余等待的车辆数
    def count_remained_car(self):
        count = 0
        for i in range(self._waitline_num):
            while self._waitline[i].is_empty() == False:
                self._waitline[i].dequeue()
                count +=1
        return count

    # 检查是否有空的等待队列
    def find_empty_waitline(self):
        empty_waitline = []
        for i in range(self._waitline_num):
            if self._weight[i] == 0:
                empty_waitline.append(i)
        return empty_waitline

    def find_not_empty_waitline(self):
        not_empty_waitline = []
        for i in range(self._waitline_num):
            if not self._waitline[i].is_empty():
                not_empty_waitline.append(i)
        return not_empty_waitline

    def dequeue_earliest_car(self):
        not_empty_waitline = self.find_not_empty_waitline()
        if not_empty_waitline !=[]:
            earliest_car_waitline_index = not_empty_waitline[0]
            for i in not_empty_waitline:
                if  self._waitline[i].top() < self._waitline[earliest_car_waitline_index].top():
                    earliest_car_waitline_index = i
            return self._waitline[earliest_car_waitline_index].dequeue()
        else:
            return None

