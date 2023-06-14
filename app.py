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
   return "<h1>Hello Jew, "+hostname+", "+ipAddr+"</h1>"

@app.route('/mobileapp')
def mobileapp():
   return "<h1>This is return from mobile app.</h1>"

@app.route('/ceda7485-55a3-429f-a589-97ccca62ca25.html')
def uuidchecking():
   return ""

@app.route('/forti-uuid.html')
def uuidDetailCheck():
   return "<forti-uuid hidden>ceda7485-55a3-429f-a589-97ccca62ca25</forti-uuid>"

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)
