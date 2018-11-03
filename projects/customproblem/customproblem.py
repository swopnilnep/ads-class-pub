from abc import ABC, abstractmethod

class College:

    def __init__(self, name:str, budget=0, depts={}):
        self._name = name
        self._budget = budget
        self._departments = depts

    def __eq__(self, other:object):
        name_eq = self._name == other._name
        budget_eq = self._budget == other._budget
        dept_eq = self._departments == other._departments
        return name_eq and budget_eq and dept_eq

    def __str__(self):
        return "Name: {}\nBudget: {}\nDepartments: {}".format(self._name, self._budget, list(self._departments.keys()))

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    name = property(get_name, set_name)

    def add_department(self, dept:object):
        if dept.name in self._departments.keys(): raise NameError("Department '%s' already exists" % dept.name)
        self._departments[dept.name] = dept
        # print("Added department '%s'" % dept.name)

    def remove_department(self, name:str):
        if name not in self._departments.keys(): raise NameError("Department '%s' does not exist" % dept.name)
        del self._departments[name]
        # print("Removed department '%s'" % name)

    def get_department(self, name:str):
        return self._departments[name]

    def get_departments(self):
        return self._departments

    def set_departments(self, departments:list):
        for dept in departments:
            self.add_department(dept)

    departments = property(get_departments, set_departments)

    def set_budget(self, amount:float):
        self._budget = amount

    def get_budget(self):
        return self._budget

    def increase_dept_budget(self, dept_name:str, amount:float):
        if dept_name not in self._departments.keys(): 
            raise NameError("Department '%s' does not exist" % dept_name)
        elif amount > 0:
            self._budget -= amount
            self._departments[dept_name].budget += amount
        else: raise ValueError("Cannot allocate 0 or negative budget")

    def reduce_dept_budget(self, dept_name:str, amount:float):
        if dept_name not in self._departments.keys(): 
            raise NameError("Department '%s' does not exist" % dept_name)
        elif amount > 0:
            self._budget += amount
            self._departments[dept_name].budget -= amount
        else: raise ValueError("Cannot allocate 0 or negative budget")

    budget = property(get_budget, set_budget)

class Department():

    def __init__(self, name:str, budget=0, professors={}, students={}):
        self._name = name
        self._budget = 0
        self._professors = professors
        self._students = students

    def __str__(self):
        return "Name: {}\nBudget: {}\nProfessors: {}\nStudents: {}".format(self._name, self._budget, list(self._professors.keys()), list(self._students.keys()))

    def __eq__(self, other:object):
        name_eq = self._name == other._name
        budget_eq = self._budget == other._budget
        professors_eq = self._professors == other._professors
        students_eq = self._students == other._students 
        return name_eq and budget_eq and professors_eq and students_eq

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    name = property(get_name, set_name)    

    def get_budget(self):
        return self._budget

    def set_budget(self, amount):
        self._budget = amount

    budget = property(get_budget, set_budget)

    def add_professor(self, prof:object):
        self._professors[prof.name] = prof

    def get_professor(self, prof_name):
        return self._professors[prof_name]

    def get_professors(self):
        return self._professors 

    def set_professors(self, profs:list):
        for prof in profs:
            self.add_professor(prof)

    professors = property(get_professors, set_professors)

    def add_student(self, stud:object):
        self._students[stud.name] = stud

    def get_student(self, stud_name):
        return self._students[stud_name]

    def get_students(self):
        return self._students

    def set_students(self, studs:list):
        for stud in studs:
            self.add_student(stud)

    students = property(get_students, set_students)

class Member(ABC):

    @abstractmethod
    def __init__():
        super().__init__()

    def set_name(self, name):
        self._name = name
    
    def get_name(self):
        return self._name 

    @abstractmethod
    def __eq__():
        return NotImplementedError

    @abstractmethod
    def __str__():
        return NotImplementedError

    name = property(get_name, set_name)

    def get_salary(self):
        return self._salary
    
    def set_salary(self, amount:float):
        self._salary = amount    

    salary = property(get_salary, set_salary)

    def get_paid(self):
        self._account += self._salary 

    @property
    def account(self):
        return self._account 

class Professor(Member):

    def __init__(self, name:str):
        self._name = name 
        self._salary = 0
        self._account = 0
        self._teaching_hours = 0

    def __str__(self):
        return "Name: {}\nTeaching Hours: {}\n Salary: {}\n Account: {}".format(self._name, self._teaching_hours, self._salary, self._account)

    def __eq__(self, other:object):
        name_eq = self._name == other._name 
        teaching_hours_eq = self._teaching_hours == other._teaching_hours
        salary_eq = self._salary == other._salary
        account_eq = self._account == other._account

        return name_eq and teaching_hours_eq and salary_eq and account_eq
    
    def teach(self, hours):
        self._teaching_hours += hours 

    @property
    def teaching_hours(self):
        return self._teaching_hours

class Student(Member):
    
    def __init__(self, name:str):
        self._name = name
        self._study_hours = 0
        self._salary = 3000
        self._account = 0

    def __str__(self):
        return "Name: {}\nStudy Hours: {}\n Salary: {}\n Account: {}".format(self._name, self._study_hours, self._salary, self._account)

    def __eq__(self, other:object):
        name_eq = self._name == other._name 
        study_hours_eq = self._study_hours == other._study_hours 
        salary_eq = self._salary == other._salary
        account_eq = self._account == other._account

        return name_eq and study_hours_eq and salary_eq and account_eq

    def study(self, hours):
        self._study_hours += hours

    @property 
    def study_hours(self):
        return self._study_hours 


# def main():

    # d1 = Department("Computer Science")
    # d2 = Department("Biology")
    # d3 = Department("Mathematics")
    # d4 = Department("Psychology")
    # d5 = Department("Data Science")


    # c1 = College("Luther College", 120000000)
    # c1.departments = [d1, d2, d3, d4]
    # c1.add_department(d5)
    # c1.increase_dept_budget("Computer Science", 12000000)

    # p1 = Professor("Roman")
    # p2 = Professor("Giang")
    # p3 = Professor("Juli")
    # p4 = Professor("Tho")

    # d1.add_professor(p1)
    # d1.add_professor(p2)
    # d1.add_professor(p3)
    # d1.professors[p4.name] = p4

    # # s1 = Student("Hiroto")
    # # s2 = Student("Phuong Anh")
    # # s3 = Student("Paul Mattson")
    # # s4 = Student("Brad Miller")
    # # s5 = Student("Kent Lee")

    # # d1.students = s1, s2, s3, s4, s5

    # print(d1)
# if __name__=="__main__":
#     main()