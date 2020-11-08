from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    outStr = """
    <html>
        <head>
            <title>Test</title>
        </head>
        <body>
            <form action="/hello_post" method="POST">
                <label>Who are you?</label>
                <br>
                <input name="username">
                <br>
                <button type="submit">Submit</button>
            </form> 
    """
    if request.method == 'GET':
        outStr += """
        </body>
    </html>
        """
    elif request.method == 'POST':
        username = request.form.get('username')

        outStr += """
        <div>
            Hello %s !
        </div>
        """%(username)

        outStr += """
        </body>
    </html>
        """
    return outStr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
