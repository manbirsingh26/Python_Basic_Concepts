import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="iwannabeaexpertengineer")

mycursor = mydb.cursor()

#mycursor.execute("Create database Manbirdb")

mycursor.execute("Show databases")

for db in mycursor:
    print(db)

