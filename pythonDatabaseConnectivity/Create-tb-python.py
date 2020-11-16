import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="mycompany")
mycursor=mydb.cursor()
mycursor.execute("show tables")

for db in mycursor:
    print(db)
