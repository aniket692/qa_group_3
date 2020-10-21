from flask import Flask, Response
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

@app.route('/connect2db')
def connect2db():
    check = connect_to_database()
    data = check.db_check()
    return Response(data, status=200, mimetype='application/json')

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
