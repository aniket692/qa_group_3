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
        message = "Connected to DB"
    except mysql.connector.Error as e:
      message = e


    #myresult = mycursor.fetchall()
    # data = '{"Message" = "'+message+'"}'
    data = message
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
      message = '200'
    else:
      message = '404'

    #myresult = mycursor.fetchall()
    #print(myresult)
    #r = [dict((mycursor.description[i][0], value) for i, value in enumerate(row)) for row in mycursor.fetchall()]
    #output = json.dumps(r)
    return message

  def db_store(self,data):
    my_db = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="ppp",
      database="db_grad_cs_1917"
    )
    data_json = json.loads(data)
    instrument_name = data_json['instrumentName']
    mycursor = my_db.cursor()
    instrument_query = 'SELECT instrument_id FROM db_grad_cs_1917.instrument where instrument_name = "'+instrument_name+'";'
    mycursor.execute(instrument_query)
    instrument_result = mycursor.fetchone()[0]
    #print(my_result)
    ctpy_name = data_json['cpty']
    mycursor = my_db.cursor()
    ctpy_query = 'SELECT counterparty_id FROM db_grad_cs_1917.counterparty where counterparty_name ="'+ctpy_name+'";'
    mycursor.execute(ctpy_query)
    ctpy_result = mycursor.fetchone()[0]
    #print(ctpy_result)
    if (ctpy_result is not None and instrument_result is not None):
      print("data present")
      mycursor = my_db.cursor()
      sql = "INSERT INTO deal (deal_time, deal_counterparty_id,deal_instrument_id,deal_type,deal_amount,deal_quantity) VALUES (%s, %s,%s, %s,%s,%s)"
      val = (data_json['time'],ctpy_result,instrument_result,data_json['type'],data_json['price'],data_json['quantity'])
      mycursor.execute(sql, val)
      my_db.commit()
      print(mycursor.rowcount,"record inserted")

  if __name__=='__main__':
    check = db_check(True)
    print(check)

