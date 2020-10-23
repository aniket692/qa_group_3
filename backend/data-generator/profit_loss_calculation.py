import mysql.connector
import json

class profit_loss:
    def calculacte_profit_loss(self):
        my_db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="ppp",
            database="db_grad_cs_1917"
        )

        my_cursor = my_db.cursor()

        #my_cursor.execute("SELECT buys.deal_counterparty_id, total_sells - total_buys as win_or_loss from (SELECT deal_counterparty_id,sum(deal_amount) as total_buys FROM db_grad_cs_1917.deal WHERE deal_type='B' group by deal_counterparty_id) as buys INNER JOIN (SELECT deal_counterparty_id,sum(deal_amount) as total_sells FROM db_grad_cs_1917.deal WHERE deal_type='S' group by deal_counterparty_id) as sells ON buys.deal_counterparty_id=sells.deal_counterparty_id ;")

        sql_query = """SELECT buys.deal_counterparty_id, total_sells - total_buys as win_or_loss
            from (SELECT deal_counterparty_id,sum(deal_amount) as total_buys
            FROM db_grad_cs_1917.deal WHERE deal_type='B' group by deal_counterparty_id) as buys
            INNER JOIN
            (SELECT deal_counterparty_id,sum(deal_amount) as total_sells
            FROM db_grad_cs_1917.deal WHERE deal_type='S' group by deal_counterparty_id)
            as sells ON buys.deal_counterparty_id=sells.deal_counterparty_id ;"""


        my_cursor.execute(sql_query)

        r = [dict((my_cursor.description[i][0], float(value)) for i, value in enumerate(row)) for row in my_cursor.fetchall()]

        return r

        #myresult = my_cursor.fetchall()


if __name__ == "__main__":
    total_profit_loss = profit_loss()
    total_profit_loss_json = json.dumps(total_profit_loss.calculacte_profit_loss())
    print(total_profit_loss_json)