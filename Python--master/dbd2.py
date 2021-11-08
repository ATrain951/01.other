import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="demo",
  password="Demo",
  database="mydatabase3"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers1 (name VARCHAR(255), address VARCHAR(255))")