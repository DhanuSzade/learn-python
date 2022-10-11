class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember:{}'.format(self.name))
    def tell(self):
        '''Tell my Details.'''
        print('Name:"{}"Age:"{}"'.format(self.name, self.age))
class Teacher(SchoolMember):
    '''Represents Teacher.'''
    def __init__(self, name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('Initialized Teacher:{})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('salary:"{}"'.format(self.salary))
class Student(SchoolMember):
    '''Represents Student.'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self, name, age)
        self.marks= marks
        print('(Initialized Student:{})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks:{}'.format(self.marks))
t= Teacher('Mr.Shree',40,60000)
s= Student('swapnil',25,85)
t.tell()
s.tell()
