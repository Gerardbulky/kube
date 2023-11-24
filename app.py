
from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/details")
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
    except:
        return 'Unable to get Hostname and IP'
    return render_template('details.html', host_name=host_name,host_ip=host_ip)

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)