from Customs_Simulation_Base_Class import Simulation,Event,Waitline
from random import randint
from PriorityQueue_heaps import PrioQueue
from Queue_SequenseList import squeue
########################################################################
#海关模拟系统
#首先分析海关系统需要维护的属性及方法
#属性：
#   实际驱动模拟的Simulation对象
#   车辆等待队列：waiteline
#   检查通道
#   总的等待时间
#   总的检查时间
#   车辆数目
#   到达时间区间
#   检查时间区间
#方法：
#   等待时间累积
#   检查时间累积
#   车辆计数
#   添加事件
#   当前时间
#   车辆入队
#   检查队列中是否还有车辆
#   下一辆车
#   寻找空闲的通道
#   释放通道
########################################################################
class Customs:
    def __init__(self,gate_num,duration,arrival_interval,check_interval):
        self.simulation = Simulation(duration) #初始化总的仿真时间
        self.waitline = Waitline(gate_num)
        self.duration = duration
        self.gates = [0] * gate_num
        self.total_wait_time = 0
        self.totol_used_time = 0
        self.car_num = 0
        self.arrival_interval = arrival_interval
        self.check_interval = check_interval
    def wait_time_acc(self,n):
        self.total_wait_time += n
    def total_time_acc(self,n):
        self.totol_used_time +=n
    def car_count_1(self):
        self.car_num +=1
    def add_event(self,event):
        self.simulation.add_event(event)
    def cur_time(self):
        return self.simulation.cur_time()
    def enqueue(self,waitline_index,car):
        self.waitline.enqueue(waitline_index,car)
    # 检查每个等待队列的是否都有等待,检查空的等待队列
    def find_empty_waitlines(self):
        empty_waitlines = self.waitline.find_empty_waitline()
        return empty_waitlines
    # 检查gate_index对应的等待队列是否有车
    def has_queued_car(self,gate_index):
        return self.waitline.has_queued_car(gate_index)
    def next_car(self,gate_index): #出队的是当前空闲的通道所对应的等待队列
        return self.waitline.dequeue(gate_index)
    #寻找空的通道
    def find_gate(self,gate_indexs):
        for i in gate_indexs:
            if self.gates[i] == 0:
                self.gates[i] = 1
                return i
        return None
    #寻找最少的排队车辆队列
    def find_waitline(self):
        temp = 0
        waitline_weight = self.waitline.get_waitline_weight()
        for i in range(self.waitline.get_waitline_num()):
            if waitline_weight[i] < waitline_weight[temp]:
                temp = i
            return temp


    def free_gate(self,i):
        if self.gates[i] == 1:
            self.gates[i] = 0
        else:
            raise ValueError('Clear gate error')

    #再定义两个方法来实施模拟和输出统计数据
    def simulate(self):
        Arrive(0,self) #初始生成一辆车
        self.simulation.run()
        self.statistics()
    def statistics(self):
        print("Simulate " + str(self.duration) + ' minutes, for ' + str(len(self.gates)) + ' gates')
        print(self.car_num, 'cars pass the customs')
        print('Average waiting time: ', self.total_wait_time / self.car_num)
        print('Average passing time: ', self.totol_used_time / self.car_num)
        remained_car_num = self.waitline.count_remained_car()
        print(remained_car_num,'cars are in waiting line')

#为了看到模拟过程发生的情况，定义一个日志输出条目
def event_log(time,name):
    print("Event: " + name + ', happens at '+ str(time))
    pass



#排队队列里的对象是车辆，类Car实现这种对象
class Car:
    def __init__(self,arrive_time):
        self.time = arrive_time
    def arrive_time(self):
        return self.time

#最后定义可能发生的事件类
#车辆到达
#车辆离开

class Arrive(Event):
    def __init__(self,arrive_time,customs):
        Event.__init__(self,arrive_time,customs)
        customs.add_event(self)
    def run(self):
        time, customs = self.time(),self.host()
        event_log(time,"car arrive")
        #生成下一个事件
        Arrive(time + randint(*customs.arrival_interval), customs)
        #下面是本到达车辆事件的行为
        car = Car(time)
        #检查是否有空的等待队列
        empty_waitlines = customs.find_empty_waitlines()
        if empty_waitlines == []:             #if customs.all_has_queued_car(): #当前有车辆排队，则新到的车辆加入排队
            waitline_index = customs.find_waitline()
            customs.enqueue(waitline_index,car)
            return
        else:
            i = customs.find_gate(empty_waitlines)
            if i is not None:
                event_log(time,'car check')
                Leave(time + randint(*customs.check_interval),i, car,customs)
            else:
                waitline_index = empty_waitlines[0] #或者检索最少的等待队列customs.find_waitline()
                customs.enqueue(waitline_index,car) #如果当前没有车辆排队，但是每个通道都在检查，则当前车辆加入排队

class Leave(Event):
    def __init__(self,leave_time,gate_index,car,customs):
        Event.__init__(self,leave_time,customs)
        self.car = car
        self.gate_index = gate_index
        customs.add_event(self)
    def run(self):
        time,customs = self.time(),self.host()
        event_log(time,'car leave')
        customs.free_gate(self.gate_index)
        customs.car_count_1()
        customs.total_time_acc(time - self.car.arrive_time())
        if customs.has_queued_car(self.gate_index):   #检查当前通道对应的等待队列是否有车
            car = customs.next_car(self.gate_index)
            i =  customs.find_gate([self.gate_index])
            event_log(time,'car check')
            customs.wait_time_acc(time - car.arrive_time())
            Leave(time+randint(*customs.check_interval),self.gate_index,car,customs)

################################################################
#启动模拟
###############################################################
car_arrival_interval = (1,2)
car_check_interval = (3,5)
cus = Customs(3,480,car_arrival_interval,car_check_interval)
cus.simulate()


######################################
#多等待队列的方案改出来了，但是模拟出来的等待时间和平均检查时间反而比较高，这是为什么呢？