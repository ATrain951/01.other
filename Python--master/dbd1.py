import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="demo",
  password="Demo"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase4")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
