import oracledb

def get_connection():
    return oracledb.connect(
        user="nuray",
        password="12345",
        dsn="localhost/ORCL1"
    )
