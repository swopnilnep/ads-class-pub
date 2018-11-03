'''
Testing the module customproblem
Swopnil N. Shrestha, 2018
'''

#!/usr/bin/python3

import pytest
from customproblem import College, Department, Member, Professor, Student

class TestCustomProblem:
    '''Testing module custom_problem'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        self.c1 = College("Luther College")
        self.c2 = College("Other College")
        self.d1 = Department("Computer Science")
        self.d2 = Department("Not Computer Science")
        self.p1 = Professor("Monty Python")
        self.p2 = Professor("Python Monty")
        self.s1 = Student("Monty Monty")
        self.s2 = Student("Python Python")

    def test_college_init(self):
        '''Test College __init__ method'''
        assert self.c1.name
        assert self.c1.budget
        assert self.c1.departments

    def test_department_init(self):
        '''Test Department __init__ method'''
        assert self.d1.name
        assert self.d1.budget
        assert self.d1.professors
        assert self.d1.students

    def test_professor_init(self):
        '''Test Professor __init__ method'''
        assert self.p1.teaching_hours

    def test_student_init(self):
        '''Test Professor __init__ method'''
        assert self.s1.study_hours

    def test_College_name(self):
        '''Test College data property getter'''
        assert self.c1.name == 'Luther College'
        assert isinstance(self.c1.name, str)

        assert self.c1.name == 'Other College'
        assert isinstance(self.c2.name, str)

    def test_Department_name(self):
        '''Test Department data property getter'''
        assert self.d1.name == 'Computer Science'
        assert isinstance(self.d1.name, str)

        assert self.d2.name == 'Not Computer Science'
        assert isinstance(self.d2.name, str)

    def test_Professor_name(self):
        '''Test Department data property getter'''
        assert self.p1.name == 'Monty Python'
        assert isinstance(self.p1.name, str)

        assert self.d2.name == 'Python Monty'
        assert isinstance(self.p2.name, str)

    def test_Student_name(self):
        '''Test Department data property getter'''
        assert self.s1.name == 'Monty Monty'
        assert isinstance(self.p1.name, str)
        assert self.s2.name == 'Python Python'
        assert isinstance(self.p2.name, str)

    def test_college_init(self):
        '''Test College __init__ method'''
        assert self.c1.name
        assert self.c1.budget
        assert self.c1.departments

    def test_professor_init(self):
        '''Test Professor __init__ method'''
        assert self.p1.teaching_hours

if __name__ == '__main__':
    pytest.main(['test_customproblem.py'])