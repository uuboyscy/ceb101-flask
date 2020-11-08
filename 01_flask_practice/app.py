from flask import Flask, request

app = Flask(__name__)

@app.route('/hello/Allen')
def hello():
    return 'Hello Allen!'
@app.route('/hello/Ted')
def hello2():
    return 'Hello Ted!'

@app.route('/hello/<username>')
def hello_username(username):
    return 'Hello %s !'%(username)

@app.route('/hello/<username>/<age>')
def hello_username_age(username, age):
    outStr = 'Hello %s, you are %s years old.'%(username, age)
    return outStr

@app.route('/query/<username>/<age>')
def query(username, age):
    outStr = """SELECT * FROM db.table WHERE username='%s' AND age=%s;"""%(username, age)
    return outStr

@app.route('/query')
def query_par():
    username = request.args.get('username')
    age = request.args.get('age')
    if username == None:
        return "<h1>What is your name ?</h1>"
    if age == None:
        outStr = "<h1>Hello %s.</h1>" % (username)
        return outStr
    outStr = "<h1>Hello %s, you are %s years old.</h1>"%(username, age)
    return outStr

@app.route('/add')
def add():
    x = request.args.get('x')
    y = request.args.get('y')
    return str(int(x) + int(y))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)