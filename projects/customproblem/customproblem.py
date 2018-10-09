class College:

    def __init__(self, name:str, budget=0, depts={}):
        self._name = name
        self._budget = budget
        self._departments = depts

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

    def increase_budget(self, dept_name:str, amount:float):
        if dept_name not in self._departments.keys(): 
            raise NameError("Department '%s' does not exist" % dept_name)
        elif amount > 0:
            self._budget -= amount
            self._departments[dept_name].budget += amount
        else: raise ValueError("Cannot allocate 0 or negative budget")

    def reduce_budget(self, dept_name:str, amount:float):
        if dept_name not in self._departments.keys(): 
            raise NameError("Department '%s' does not exist" % dept_name)
        elif amount > 0:
            self._budget += amount
            self._departments[dept_name].budget -= amount
        else: raise ValueError("Cannot allocate 0 or negative budget")

    budget = property(get_budget, set_budget)
class Department():

    def __init__(self, name:str, budget=0, instructors={}, students={}):
        self._name = name
        self._budget = 0
        self._instructors = {}
        self._students = {}

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return "Name: {}\nBudget: {}".format(self._name, self._budget)

    def get_name(self):
        return self._name

    name = property(get_name, set_name)    

    def get_budget(self):
        return self._budget

    def set_budget(self, amount):
        self._budget = amount

    budget = property(get_budget, set_budget)
class Member():

    def __init__(self, name, study_hours=0, salary=0, money=0):
        self._name = name 
        self._study_hours = 0
        self._salary = 0
        self._money = 0

    def set_name(self, name):
        self._name = name
    
    def get_name(self):
        return self._name 

    name = property(get_name, set_name)

    def get_salary(self):
        return self._salary
    
    def set_salary(self, amount:float):
        self._salary = amount    

    salary = property(get_salary, set_salary)

    def get_paid(self):
        self._money += salary 

    def study(self, hours):
        self._hours_studied += hours

class Professor(Member):

    def __init__(self, name:str):
        super().__init__(name)
        self._age = None 
        self._teaching_hours = 0

    def teach(self, hours):
        self._teaching_hours += hours 

    def change_salary(self, amount):
        super().set_salary(amount)

# class student(Member):
#     def __int__(name):
#         super().__init__(name)


def main():
    # d1 = Department("Computer Science")

    # c1 = College("Luther College", 120000000)
    # c1.add_department(d1)

    # print(c1.budget)
    
    # c1.increase_budget('Computer Science', 60000000)
    # print(c1.departments['Computer Science'])

    # print(c1.budget)

    p1 = Professor("Swopnil")
    print(p1.get_name())

if __name__=="__main__":
    main()


