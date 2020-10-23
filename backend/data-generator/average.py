import mysql.connector
import json
import datetime
class connect_to_database:
  def average(self, deal_type, deal_instrument_id, start_time, end_time):
    my_db = None
    try:
      my_db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="ppp",
        database="db_grad_cs_1917"
      )
      query = ('SELECT deal_instrument_id, sum(deal_amount * deal_quantity) / sum(deal_quantity) AS average FROM db_grad_cs_1917.deal WHERE deal_time BETWEEN "' + start_time + '" AND "'+ end_time + '" AND deal_type = "'+ deal_type + '" AND deal_instrument_id = "'+str(deal_instrument_id)+'" GROUP BY deal_instrument_id ORDER BY deal_instrument_id')
      if my_db.is_connected():
        cursor = my_db.cursor()
        cursor.execute(query)
        #averageres = cursor.fetchall()
        #print(averageres)
        for (average) in cursor:
          return(average[1])
    except mysql.connector.Error as e:
      return str(e)

    cursor.close();
    my_db.close();

  def averagebuysell(self, deal_instrument_id, start_time, end_time):
    return average(True, "B", deal_instrument_id, start_time, end_time) + average(True, "S", deal_instrument_id, start_time, end_time)


  if __name__=='__main__':
    avg_s = average(True, "S", 1002,  '2017-07-28T18:00:00.955', '2017-07-28T18:10:29.955')
    avg_b = average(True, "B", 1002, '2017-07-28T18:00:00.955', '2017-07-28T18:10:29.955')
    averagebuysell(True, 1002, '2017-07-28T18:00:00.955', '2017-07-28T18:10:29.955')
    # print("avgbs ",                )
    print(avg_s, avg_b)

