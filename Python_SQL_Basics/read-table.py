import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="iwannabeaexpertengineer", database="Manbirdb")

mycursor = mydb.cursor()

#mycursor.execute("use Manbirdb")

mycursor.execute("Select * from employee")
myresult = mycursor.fetchall()

#myresult = mycursor.fetchone()

for row in myresult:
    print(row)