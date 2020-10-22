import mysql.connector
import json

class endposition:
    def calculate_endposition(self):
        my_db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="ppp",
            database="db_grad_cs_1917"
        )

        my_cursor = my_db.cursor()

        #my_cursor.execute("SELECT buys.deal_counterparty_id, total_sells - total_buys as win_or_loss from (SELECT deal_counterparty_id,sum(deal_amount) as total_buys FROM db_grad_cs_1917.deal WHERE deal_type='B' group by deal_counterparty_id) as buys INNER JOIN (SELECT deal_counterparty_id,sum(deal_amount) as total_sells FROM db_grad_cs_1917.deal WHERE deal_type='S' group by deal_counterparty_id) as sells ON buys.deal_counterparty_id=sells.deal_counterparty_id ;")

        sql_query = """ 
        SELECT buys.deal_counterparty_id, buys.deal_instrument_id, instrument_name ,
        sum(total_sells) - sum(total_buys) as endposition, sum(sells.total_sell_quantity) - sum(buys.total_buy_quantity) as total_quantity
        from ((SELECT deal_counterparty_id,deal_instrument_id,sum(deal_amount) as total_buys, 
        sum(deal_quantity) as total_buy_quantity
        FROM db_grad_cs_1917.deal WHERE deal_type='B' group by deal_counterparty_id, deal_instrument_id
        order by deal_counterparty_id) as buys
        INNER JOIN
        (SELECT deal_counterparty_id,deal_instrument_id,sum(deal_amount) as total_sells, sum(deal_quantity) as total_sell_quantity
        FROM db_grad_cs_1917.deal WHERE deal_type='S' group by deal_counterparty_id, deal_instrument_id
        order by deal_counterparty_id)
        as sells ON buys.deal_instrument_id=sells.deal_instrument_id), instrument 
        where instrument.instrument_id = buys.deal_instrument_id
        group by buys.deal_counterparty_id, buys.deal_instrument_id ;
        """


        my_cursor.execute(sql_query)

        r = [dict((my_cursor.description[i][0], str(value)) for i, value in enumerate(row)) for row in my_cursor.fetchall()]

        return r

        #myresult = my_cursor.fetchall()


if __name__ == "__main__":
    total_endposition = endposition()
    total_endposition_json = json.dumps(total_endposition.calculate_endposition())
    print(total_endposition_json)