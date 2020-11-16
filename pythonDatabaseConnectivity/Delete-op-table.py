import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="mycompany")
mycursor=mydb.cursor()

sql="delete from employee where name='sandeep'"

mycursor.execute(sql)
mydb.commit()