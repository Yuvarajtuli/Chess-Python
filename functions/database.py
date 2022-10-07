import pyodbc as sql
conn = ''
getResult = []
def connect():
    global conn
    cnxn_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=DESKTOP-PACUU73\MSSQLSERVER02;"
            "Database=chess;"
            "Trusted_Connection=yes;")
    conn = sql.connect(cnxn_str)
    if conn:
        return "connected!"
    else:
        return "not connected!"
def insert(query):
    global conn
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
def delete(query):
    global conn
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
# connect()
# insert("insert into serverState (serverName) values ('chessyt')")
