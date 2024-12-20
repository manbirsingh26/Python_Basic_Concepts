import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="iwannabeaexpertengineer", database="Manbirdb")

mycursor = mydb.cursor()

#mycursor.execute("use Manbirdb")

#sql = "UPDATE employee SET sal=150000 WHERE name='manbir'"
sql1 = "UPDATE employee SET name='jasleen' WHERE name='ankita'"


mycursor.execute(sql1)

mydb.commit()
