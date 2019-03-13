# 练习 定义一个类Time
class TimeTypeError(TypeError):
    pass
class TimeValueError(ValueError):
    pass
class Time:
    #初始化
    def __init__(self,hours,minutes,seconds):
        if hours > 23 or hours < 0:
            raise TimeValueError('wrong hour value,should be in 0 to 23 !')
        if minutes >59 or minutes < 0:
            raise TimeValueError('wrong minute value,should be in 0 to 59 !')
        if seconds >59 or seconds < 0:
            raise TimeValueError('wrong hour second,should be in 0 to 59 !')
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
    def hours(self):
        return self._hours
    def minutes(self):
        return self._minutes
    def seconds(self):
        return self._seconds
    def __str__(self):
        return ':'.join((str(self._hours),str(self._minutes),str(self._seconds)))
    def __add__(self,another):
        if not isinstance(another,Time):
            raise TimeTypeError('wrong Type:',another)
        seconds = (self._seconds + another._seconds) % 60
        carry = (self._seconds + another._seconds) // 60
        minutes = (carry + self._minutes + another._minutes) % 60
        carry = (carry + self._minutes + another._minutes) // 60
        hours = (carry + self._hours + another._hours) % 24
        carry = (carry + self._hours + another._hours) // 24
        return Time(hours,minutes,seconds)
    def __sub__(self,another):
        if not isinstance(another,Time):
            raise TimeTypeError('wrong Type:',another)
        carry_s = 0
        carry_m = 0
        carry_h = 0
        if self._seconds < another._seconds:
            carry_s = 1
        seconds = carry_s * 60 + self._seconds - another._seconds
        if self._minutes < another._minutes + carry_s:
            carry_m = 1
        minutes = carry_m * 60 + self._minutes - another._minutes -carry_s
        if self._hours < another._hours + carry_m:
            carry_h = 1
        hours = 24 * carry_h + self._hours - another._hours - carry_m
        return Time(hours,minutes,seconds)
    def __eq__(self,another):
        if not isinstance(another,Time):
            raise TimeTypeError('wrong Type:',another)
        if self._hours == another._hours and self._minutes == another._minutes and self._seconds == another._seconds:
            return True
        else:
            return False
    def __lt__(self,another):
        if not isinstance(another,Time):
            raise TimeTypeError('wrong Type:',another)
        if self._hours < another._hours:
            return True
        elif self._hours == another._hours:
            if self._minutes < another._minutes:
                return True
            elif self._minutes == another._minutes:
                if self._seconds < another._seconds:
                    return True
        else:
            return False
'''
#测试
t1 = Time(12,15,15)
t2 = Time(13,14,15)
t3 = Time(12,15,15)
print(t1)
print(t3 == t1)
print(t1 < t2)
print(t2 -t1)
print(t3 + t1)
'''