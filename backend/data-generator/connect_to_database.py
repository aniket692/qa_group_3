import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="ppp",
  database="db_grad_cs_1917"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM db_grad_cs_1917.users;")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


