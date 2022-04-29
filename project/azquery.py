import pyodbc

# Specifying the ODBC driver, server name, database, etc. directly
conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.9.so.1.1};SERVER=X.database.windows.net;DATABASE=myDB1;UID=azuresql;PWD='{password1}')
import pyodbc
server = 'X.database.windows.net '
database = 'DemoDatabase'
username = '{username}'
password = '{password1}' 
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

