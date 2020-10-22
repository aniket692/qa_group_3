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
      message = e


    #myresult = mycursor.fetchall()
    data = '{"Message" = "'+message+'"}'
    return data
    #for x in myresult:
    #  print(x)
  def db_login_check(self,username,password):
    my_db = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="ppp",
      database="db_grad_cs_1917"
    )
    mycursor = my_db.cursor()
    query = 'SELECT * FROM db_grad_cs_1917.users where user_id = "'+username+'" and user_pwd="'+password+'";'
    print(query)
    mycursor.execute(query)
    row_count=mycursor.fetchone()
    if row_count != None:
      #rs = mycursor.fetchall()
      message = '{"code" = "200"}'
    else:
      message = '{"code"="404"}'

    #myresult = mycursor.fetchall()
    #print(myresult)
    #r = [dict((mycursor.description[i][0], value) for i, value in enumerate(row)) for row in mycursor.fetchall()]
    #output = json.dumps(r)
    return message


  if __name__=='__main__':
    check = db_check(True)
    print(check)

