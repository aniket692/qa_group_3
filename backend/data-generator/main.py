from flask import Flask, Response, request
from flask_cors import CORS
import webServiceStream
from connect_to_database import connect_to_database
from RandomDealData import *
from average import average_class
from endposition import endposition
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return webServiceStream.index()

@app.route('/testservice')
def testservice():
    return webServiceStream.testservice()

@app.route('/streamTest')
def stream():
    return webServiceStream.stream()

@app.route('/streamStore')
def stream_store():
    return webServiceStream.stream_store()

@app.route('/connect2db')
def connect2db():
    check = connect_to_database()
    data = check.db_check()
    return Response(data, status=200, mimetype='application/json')

@app.route('/historic_data')
def historic_data():
    check = connect_to_database()
    data = check.get_historic()
    return Response(data, status=200, mimetype='application/json')

@app.route('/profile_details')
def profile_details():
    # Fetch form data
    #userDetails = request.form
    #user = userDetails['user']
    #instrument = userDetails['instrument']
    #start = userDetails['startPeriod']
    #end = userDetails['endPeriod']
    avg_class = average_class()
    avg_s = avg_class.average("S", 1002, '2017-07-28T18:00:00.955', '2017-07-28T18:10:29.955')
    avg_b = avg_class.average("B", 1002, '2017-07-28T18:00:00.955', '2017-07-28T18:10:29.955')
    total_endposition = endposition()
    test = total_endposition.calculate_endposition()
    #total_endposition_json = json.dumps(total_endposition.calculate_endposition())
    #endposition_var = total_endposition_json[0]
    #print(end)
    data_set = {"average_sell": [str(avg_s)], "average_buy": [str(avg_b)], "endposition":[test[0]['endposition']]}
    json_dump = json.dumps(data_set)
    return Response(json_dump, status=200, mimetype='application/json')

@app.route('/login_check', methods=['GET', 'POST'])
def login_check():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        username = userDetails['user']
        password = userDetails['password']
        #print(username)
        #print("password",password)
        check = connect_to_database()
        data = check.db_login_check(username,password)
        #cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        #mysql.connection.commit()
        #cur.close()
        return Response(data, status=200, mimetype='application/json')
    else:
        return Response({'"message":no data'}, status=200, mimetype='application/json')


@app.route('/streamTest/sse')
def sse_stream():
     return webServiceStream.sse_stream()


def bootapp():
    #global rdd 
    #rdd = RandomDealData()
    #webServiceStream.bootServices()
    app.run(debug=True, port=8080, threaded=True, host=('0.0.0.0'))


if __name__ == "__main__":
      bootapp()
