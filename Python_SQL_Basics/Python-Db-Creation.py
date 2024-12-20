import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="iwannabeaexpertengineer")

print(mydb)

if mydb:
    print("Connection Successful")

else:
    print("Connection unsuccessful")
