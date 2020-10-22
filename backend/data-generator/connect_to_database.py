import mysql.connector
import json
class connect_to_database:
  def db_check(self):
    my_db = None
    try:
      my_db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="ppp",
        database="db_grad_cs_1917"
      )
      if my_db.is_connected():
        message = "connected to DB"
    except mysql.connector.Error as e:
      message = str(e)


    #myresult = mycursor.fetchall()
    data = '{"Message" = "'+message+'"}'
    return data
    #for x in myresult:
    #  print(x)

  if __name__=='__main__':
    check = db_check(True)
    #print(check)

