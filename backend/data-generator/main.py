from flask import Flask, Response, request
from flask_cors import CORS
import webServiceStream
from connect_to_database import connect_to_database
from RandomDealData import *

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
