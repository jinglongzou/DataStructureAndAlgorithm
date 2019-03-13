from Customs_Simulation_Base_Class import Simulation,Event
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
        self.waitline = squeue()
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
    def enqueue(self,car):
        self.waitline.enqueue(car)
    def has_queued_car(self):
        return not self.waitline.is_empty()
    def next_car(self):
        return self.waitline.dequeue()
    def find_gate(self):
        for i in range(len(self.gates)):
            if self.gates[i] == 0:
                self.gates[i] = 1
                return i
        return None
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
        i = 0
        while not self.waitline.is_empty():
            self.waitline.dequeue()
            i +=1
        print(i,'cars are in waiting line')

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
        if customs.has_queued_car(): #当前有车辆排队，则新到的车辆加入排队
            customs.enqueue(car)
            return
        i = customs.find_gate()
        if i is not None:
            event_log(time,'car check')
            Leave(time + randint(*customs.check_interval),i, car,customs)
        else:
            customs.enqueue(car) #如果当前没有车辆排队，但是每个通道都在检查，则当前车辆加入排队

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
        if customs.has_queued_car():
            car = customs.next_car()
            i = customs.find_gate()
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