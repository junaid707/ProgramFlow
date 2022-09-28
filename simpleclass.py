class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def full_name(self):
        self.fullname = "{} {}".format(self.first,self.last)
        return self.fullname

class Developer(Employee):
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language

class Manager(Employee):
    def __init__(self, first, last, pay, employee=None):
        super().__init__(first, last, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_employees(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_employees(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_emp(self):
        for emp in self.employee:
            print(self.first, "supervises", emp.full_name())


dev1 = Developer("Junaid", "Mansoori", 9899, "Python")
dev2 = Developer("Shabnam", "Khan", 8989, "Java")

mngr1 = Manager("Jeff", "Corey", 907878, [])
print(mngr1.email)
mngr1.print_emp()





