import pyodbc

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect(r"DRIVER={SQL Server};SERVER=nbiba.database.windows.net;DATABASE=myDB1;UID=azuresql;PWD=aezakmi1996X-")


# Create a cursor from the connection
cursor = cnxn.cursor()
def user_exists(a,b):
    
    cursor.execute("select * from users where email = ? AND password = ?",[a,b])
    row = cursor.fetchone()
    if row:
        print("found")
        

user_exists("a","a")


