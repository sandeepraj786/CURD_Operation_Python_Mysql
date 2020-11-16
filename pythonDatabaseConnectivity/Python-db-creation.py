import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
print(mydb)

if(mydb):
    print("connection succesful")
else:
    print("connection unsuccesful")