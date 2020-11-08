from flask import Flask

app = Flask(__name__, static_url_path='/static', static_folder='./static')

@app.route('/test')
def images():
    outStr = """
    <link href="/static/mycss.css" rel="stylesheet" type="text/css">
    <div class="test">
    123123123123vhcxvhcxzjlk
    </div>
    <img src="/static/google.png">
    """
    return outStr

if __name__ == '__main__':
    app.run()