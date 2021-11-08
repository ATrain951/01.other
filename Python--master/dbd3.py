import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="demo",
  password="Demo",
  database="mydatabase3"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)