from database import get_connection

def create_tables():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute(""" 
    CREATE TABLE employees2(
                ID_EMP NUMBER PRIMARY KEY,
                NAME VARCHAR2(100) NOT NULL,
                SALARY FLOAT NOT NULL,
                DEP_ID NUMBER NOT NULL
            )
        """)
    conn.commit()
    cursor.close()
    conn.close()


def id_employees(id_emp):
    if not id:
        print("id daxil olunmayib")
    else:
        return True
def name_employees(name):
    if name is None or name == "":
        print("ad daxil olunmayib")
    else:
        return True
def salary_employees(salary):
    if salary <= 0:
        print('maas duzgun qeyd olunmayib!')
    else:
        return True