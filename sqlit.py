import sqlite3
from employee import Employee
# conn = sqlite3.connect("employee.db")
conn = sqlite3.connect(":memory:")

c = conn.cursor()
c.execute(""" CREATE TABLE employee (
    first text,
    last text,
    pay integer
)""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT into employee VALUES (:first,:last,:pay)",
                  {"first": emp.first, "last": emp.last, "pay": emp.pay})


def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employee WHERE last=:last", {"last": lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employee SET pay=: pay WHERE first=: first AND last=: last """,
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


emp_1 = Employee("John", "Doe", 80000)
emp_2 = Employee("Jane", "Doe", 90000)
insert_emp(emp_1)
insert_emp(emp_2)
emps = get_emp_by_name("Doe")
print(emps)

update_pay(emp_2, 95000)
print(emps)
# c.execute("INSERT into employee VALUES ('asif','Raza',5000)")


# c.execute("INSERT into employee VALUES (?,?,?)",
#           (emp_1.first, emp_1.last, emp_1.pay))

# conn.commit()
# c.execute("INSERT into employee VALUES (:first,:last,:pay)",
#           {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})
# conn.commit()
# c.execute("SELECT * FROM employee WHERE last=?", ("Raza",))
# print(c.fetchall())
# c.execute("SELECT * FROM employee WHERE last=:last", {"last": "Doe"})
# print(c.fetchall())
# conn.commit()
conn.close()
