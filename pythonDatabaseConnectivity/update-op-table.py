import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="mycompany")
mycursor=mydb.cursor()

sql="update employee set sal=70000 where name='sandeep'"
mycursor.execute(sql)

mydb.commit()