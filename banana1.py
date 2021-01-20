import random

def convert_tuple(tup):
    str = ''.join(tup)
    return str

class Employee():
    def __init__(self, name, emp_no):
        self.name = name
        self.emp_no = emp_no
        self.schedule = []

    def __str__(self):
        return f"Name: {self.name} Employee Number: {self.emp_no}\n Schedule: {self.schedule}"


class Roster():
    def __init__(self, max_emp):
        self.emp_list = [Employee("Nate", 1), Employee("Ted", 2), Employee("Jake", 3)]
        self.max_emp = max_emp

    def input(self):
        emp_no = 1
        for n in range(self.max_emp):
            new_emp = Employee(input("Name:"), emp_no)
            self.emp_list.append(new_emp)
            emp_no += 1

    def reset(self):
        self.emp_list.clear()
        print("Roster has been reset.")

    def __str__(self):
        string = ""
        for emp in self.emp_list:
            string += str(emp)
        return string

class Schedule():
    def __init__(self, days):
        self.days = days
        self.roster = Roster(3)
        self.total_days = []

    def get_total_days(self):
        for day in range(1 , self.days + 1):
            self.total_days.append(day)

    def make(self):
        self.get_total_days()
        people = self.roster.emp_list

        while len(self.total_days) > 0:
            for person in people:
                #this extra check is necessary for if the total days divided by our employees is not an even number
                if len(self.total_days) > 0:
                    index = random.randint(0,len(self.total_days) - 1)
                    person.schedule.append(self.total_days.pop(index))

    def __str__(self):
        string = ""
        for person in self.roster.emp_list:
            string += str(person)
        return string

class Main():
    def __init__(self):
        self.s = Schedule(30)
        self.s.make()
        print(self.s)

m = Main()
