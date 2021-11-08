import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="demo",
  password="Demo",
  database="mydatabase3"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers1_2")

myresult = mycursor.fetchall()
'''
for x in myresult:
  print(x)
'''
for x in mycursor:
  print(x)
