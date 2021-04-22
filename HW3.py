from flask import Flask, render_template, send_from_directory
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user": generate_password_hash("user"),
    "guest": generate_password_hash("guest")
}

@app.route('/static/<path:path>')
def index13(path):
    return send_from_directory('static', path)

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False
    
@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


@app.route('/cabinet/')
@auth.login_required
def index1():
    return render_template("HW3.html")
    #"Hello, %s!" % auth.username()


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)