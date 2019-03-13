# 在实现这些类之前，需要定义一些异常类，以便在定义人事类的操作中遇到的
# 异常情况时引发特殊的异常，使用这些类的程序部分可以正确的捕捉和处理
class personTypeError(TypeError):
    pass
class personValueError(ValueError):
    pass

import datetime

# 基类 person
class person(object):
    # 人数统计
    _num = 0

    # 初始化
    def __init__(self, name=None, sex=None, birthday=None, ident=None):
        if not (isinstance(name, str)) and sex in ('男', '女'):
            raise personTypeError
        try:
            birth = datetime.date(*birthday)  # 这个*号是必须的，它的含义目前不清楚
        except:
            raise personValueError('Wrong date: ', birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._ident = ident
        person._num += 1

    def ident(self):
        return self._ident

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._birthday

    def age(self):
        return datetime.date.today().year - self._birthday.year

    def set_name(self, name):
        if not isinstance(name, str):
            raise personTypeError('set_name: ', name)
        self._name = name

    # 比较
    def __lt__(self, another):
        if not isinstance(another, person):
            raise personTypeError(another)
        return self._ident < another._ident

    # 定义一个类方法，便与取出人员数
    @classmethod
    def num(cls):
        return person._num

    def __str__(self):
        return ' '.join((self._ident, self._name, self._sex, str(self._birthday)))

    def details(self):
        return ', '.join(('编号：' + self._ident, '姓名：' + self._name,
                          '性别：' + self._sex, '出生日期：' + str(self._birthday)))

'''
# 基类测试
p1 = person('谢玉洁', '女', (1995, 7, 30), '1201510111')
p2 = person('王立强', '男', (1990, 2, 17), '1201380324')
p3 = person('张子玉', '女', (1974, 7, 30), '0197401032')
p4 = person('李国栋', '男', (1962, 5, 24), '0196212018')

plist2 = [p1, p2, p3, p4]
for p in plist2:
    print(p)

print('\nAfter sorting: ')
plist2.sort()
for p in plist2:
    print(p)
'''

# 学生类
class student(person):
    _id_num = 0  # 用于递增编号

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return '1{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name=None, sex=None, birthday=None, department=None):
        super().__init__(name, sex, birthday, student._id_gen())
        if not isinstance(department, str):
            raise personTypeError('personTypeError: ', department)
        self._department = department
        self._courses = {}
        self._enroll_date = datetime.date.today()

    def department(self):
        return self._department

    def en_year(self):
        return self._enroll_date

    def scores(self):
        pass

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_scores(self, course_name, score):
        self._courses[course_name] = score

    def scores(self):
        return [(cname, self._course[cname]) for cname in self._courses]

    def __str__(self):
        return ' '.join((person.__str__(self), str(self._enroll_date),
                         self._department, str(self.scores())))

    def details(self):
        return ', '.join((person.details(self),
                          '入学日期：' + str(self._enroll_date),
                          '院系：' + self._department,
                          '课程记录：' + str(self.scores())))

'''
# 学生测试例
print('\n学生：')
s1 = student('谢玉洁', '女', (1995, 7, 30), '机械')
print(s1)
'''

# 教职人员类
class staff(person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return '0{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name=None, sex=None, birthday=None, entry_date=None):
        super().__init__(name, sex, birthday, staff._id_gen())
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise personValueError('wrong date: ', entry_date)
        else:
            self._entry_date = datetime.date.today()
        self._salary = 1720  # 默认最低工资
        self._department = '未定'
        self._position = '未定'

    def salary(self):
        return self._salary

    def entry_date(self):
        return self._entry_date

    def position(self):
        return self._position

    def set_salary(self, salary):
        if not isinstance(salary, int):
            raise personTypeError('personTypeError: ', salary)
        self._salary = salary

    def set_position(self, position):
        if not isinstance(position, str):
            raise personTypeError('personTypeError: ', position)
        self._position = position

    def set_department(self, department):
        self._department = department

    def __str__(self):
        return ' '.join((person.__str__(self), str(self._entry_date),
                         self._department, self._position, str(self._salary)))

    def details(self):
        return ', '.join((person.details(self),
                          '入职日期：' + str(self._entry_date),
                          '院系：' + self._department,
                          '职位：' + self._position,
                          '工资：' + str(self._salary)))

'''
# 胶教职人员测试
print('\n教职人员：')
staff1 = staff('谢玉洁', '女', (1995, 7, 30))
staff2 = staff('王立强', '男', (1990, 2, 17))
print(staff1)
print(staff2)
staff1.set_department('数学')
staff1.set_position('副教授')
staff1.set_salary(8400)

print(staff1.details())
'''