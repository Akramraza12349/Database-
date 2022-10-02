import pyodbc
import pandas as pd
from mysql.connector import Error
# cnxn = pyodbc.connect('DRIVER={SQL Server};' +
#                       'SERVER=' + "localhost" + ';' +
#                       'DATABASE=' + "master" + ';')
cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-B268QH5;DATABASE=master;')
cursor = cnxn.cursor()
cursor.execute(
    """
  CREATE TABLE Person1
  (
  P_Id int,
  LastName varchar(255),
  FirstName varchar(255),
  Address varchar(255),
  City varchar(255)
  )
  """
)
cursor.commit()


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


create_teacher_table = """
CREATE TABLE teacher1 (
  teacher_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  language_1 VARCHAR(3) NOT NULL,
  language_2 VARCHAR(3),
  dob DATE,
  tax_id INT UNIQUE,
  phone_no VARCHAR(20)
  );
 """
execute_query(cnxn, create_teacher_table)
pop_teacher = """
INSERT INTO teacher1 VALUES
(1,  'James', 'Smith', 'ENG', NULL, '1985-04-20', 12345, '+491774553676'),
(2, 'Stefanie',  'Martin',  'FRA', NULL,  '1970-02-17', 23456, '+491234567890'), 
(3, 'Steve', 'Wang',  'MAN', 'ENG', '1990-11-12', 34567, '+447840921333'),
(4, 'Friederike',  'Müller-Rossi', 'DEU', 'ITA', '1987-07-07',  45678, '+492345678901'),
(5, 'Isobel', 'Ivanova', 'RUS', 'ENG', '1963-05-30',  56789, '+491772635467'),
(6, 'Niamh', 'Murphy', 'ENG', 'IRI', '1995-09-08',  67890, '+491231231232');
"""

cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-B268QH5;DATABASE=master;')
execute_query(cnxn, pop_teacher)
from_db = []
q1 = """
SELECT *
FROM teacher1;
"""


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


results = read_query(cnxn, q1)
for result in results:
    result = list(result)
    from_db.append(result[:4])


columns = ["teacher_id", "first_name", "client_name", "language_1", ]
df = pd.DataFrame(from_db, columns=columns)
