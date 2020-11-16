import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="mycompany")
mycursor=mydb.cursor()

mycursor.execute("select name from employee")

myresult=mycursor.fetchone()

for row in myresult:
    print(row)