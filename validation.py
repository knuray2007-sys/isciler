from database import get_connection

def add_employees(id_emp, name, salary, dep_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO employees2 (ID_EMP, NAME, SALARY, DEP_ID) VALUES (:1, :2, :3, :4)",
            (id_emp, name, salary, dep_id)
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        cursor.close()
        conn.close()
