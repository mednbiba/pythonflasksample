import pyodbc

# Specifying the ODBC driver, server name, database, etc. directly
conn = pyodbc.connect(r"DRIVER={SQL Server};SERVER=nbiba.database.windows.net;DATABASE=myDB1;UID=azuresql;PWD=aezakmi1996X-")
import pyodbc
server = 'nbiba.database.windows.net'
database = 'DemoDatabase'
username = 'azuresql'
password = 'aezakmi1996X-' 
driver= '{SQL Server}'

cursor = conn.cursor()

def user_create(b,c,d):
    x=0
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO dbo.users1([email], [password], [name]) VALUES(?,?,?)",[b,c,d])
        x=1
    return x

def user_exists(a,b):
    x=0
    cursor.execute("select * from users1 where email = ? AND password = ?",[a,b])
    row = cursor.fetchone()
    if row:
        x=1
    return x

