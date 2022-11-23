class Employee:
    def __init__(self, first, last, email, salary):
        self.first = first
        self.last = last
        self.email = email
        self.salary = salary

    def fullname(self):
        return (f"{self.first} {self.last}")

    def apply_raise(self):
        self.incremented_sal = int(self.salary)*1.04
        return self.incremented_sal


emp1 = Employee("Akram", "Raza", "akram@mpminfosoft.com", 60000)

# print(emp1.first)
# print(emp1.last)
# print(emp1.email)
type(emp1.fullname())
# if we use class than we to pass instance of the class
# as an argument
print(Employee.fullname(emp1))
print(emp1.fullname())

print(emp1.incremented_sal)
print(emp1.salary)
emp1.apply_raise()
print(emp1.salary)
