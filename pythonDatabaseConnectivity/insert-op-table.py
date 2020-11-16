import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="mycompany")
mycursor=mydb.cursor()

sqlform="insert into employee(name,sal) values(%s,%s)"

employees = [("sandeep",40000),("pradeep",45000),("virat",50000)]
mycursor.executemany(sqlform,employees)
mydb.commit()




