from flask import Flask, render_template, Response, request
from flask_sse import sse
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
#app.register_blueprint(sse, url_prefix='/stream')
CORS(app)

@app.route('/deals')
def forwardStream():
    r = requests.get('http://localhost:8080/streamTest', stream=True)
    def eventStream():
            for line in r.iter_lines( chunk_size=1):
                if line:
                    yield 'data:{}\n\n'.format(line.decode())
    return Response(eventStream(), mimetype="text/event-stream")

@app.route('/client/testservice')
def client_to_server():
    r = requests.get('http://localhost:8080/testservice')
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

@app.route('/')
@app.route('/index')
def index():
    return "webtier service points are running..."


@app.route('/db_connection')
def db_connection():
    r = requests.get('http://localhost:8080/connect2db', stream=True)
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

@app.route('/login', methods=['POST'])
def login():
    # login_details = {"username":"alison","password":"gradprog2016@07"}
        # print("test")
    login_details = request.json
    print(login_details)
    r = requests.post('http://localhost:8080/login_check',data=login_details,stream=True)
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

@app.route('/dealerdata', methods=['GET','POST'])
def dealer_data():
    login_details = {"user":"selvyn","instrument":"Astronomica","startPeriod":"2017-07-28T17:00:00.955","endPeriod":"2017-07-28T18:00:00.955"}
    print("test")
    login_details = request.json
    print(login_details)
    r = requests.get('http://localhost:8080/profile_details',data=login_details,stream=True)
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")
def get_message():
    """this could be any function that blocks until data is ready"""
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

def bootapp():
    app.run(debug=True, port=8090, threaded=True, host=('0.0.0.0'))

if __name__ == '__main__':
     bootapp()
