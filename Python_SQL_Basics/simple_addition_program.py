import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="iwannabeaexpertengineer", database="Arithmetic")

mycursor = mydb.cursor()

#mycursor.execute("Create database Arithmetic")

#mycursor.execute("Show databases")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(a + b)
print("Addition is:  %.4f " % c)
#mycursor.execute("Create table addition( First_No float(25), Second_No float(25), Addition float(50))")
#mycursor.execute("Show tables")
mycursor.execute("INSERT INTO addition(First_No,Second_No,Addition) VALUES(%s,%s,%s)", (a, b, c))
#mycursor.execute("DELETE FROM addition WHERE Addition=113.78999999999999")
#mycursor.execute("Select * from addition")

#myresult = mycursor.fetchall()
#for row in myresult:
    #print(row)

mydb.commit()


#for tb in mycursor:
    #print(tb)