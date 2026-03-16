from isci_repository import create_tables
from validation import add_employees
from isci_repository import id_employees, name_employees, salary_employees

create_tables()

def main():
    while True:
            name=input("adı daxil edin: ")
            id_emp=int(input("id daxil edin: "))
            dep_id=int(input("departamenti daxil edin: "))
            salary=float(input("maas daxil edin: "))

            if not id_employees(id_emp):
                continue
            if not name_employees(name):
                continue
            if not salary_employees(salary):
                continue
            if add_employees(id_emp, name, salary, dep_id):
                print("Isci elave olundu!")
            else:
                print("Isci elave olunmadi!")
            if name=='done':
                break

main()