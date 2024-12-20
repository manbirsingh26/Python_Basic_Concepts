import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="iwannabeaexpertengineer")

mycursor = mydb.cursor()

mycursor.execute("use Manbirdb")
#mycursor.execute("Create table employee(name varchar(200), sal int(20))")
mycursor.execute("Show tables")

for tb in mycursor:
    print(tb)