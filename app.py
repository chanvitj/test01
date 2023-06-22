import socket
from flask import Flask

config = {
   "DEBUG": True
}
app = Flask(__name__)
app.config.from_mapping(config)

username="asdf"
pwd="zxcv@asdf"

@app.route('/')
def Home():
   hostname=socket.gethostname()
   ipAddr=socket.gethostbyname(hostname)
   return "<h1>Hello Jew333, "+hostname+", "+ipAddr+"</h1>"

@app.route('/mobileapp')
def mobileapp():
   return "<h1>This is return from mobile app.</h1>"

@app.route('/5.html')
def uuidchecking():
   return ""

@app.route('/forti-uui.html')
def uuidDetailCheck():
   return "<forti-uuid hidden>5</forti-uuid>"

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)
