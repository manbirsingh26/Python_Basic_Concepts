import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="iwannabeaexpertengineer", database="Manbirdb")

mycursor = mydb.cursor()

#mycursor.execute("use Manbirdb")

del1 = "DELETE FROM employee WHERE name='amit'"

mycursor.execute(del1)

mydb.commit()