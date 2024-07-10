from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)
try:
    app.config.from_pyfile('config.py')
    host = app.config['HOST']
    debug = app.config['DEBUG']
    port = app.config['PORT']
except Exception:
    host = []
    debug = True
    port = 8000

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def send_js(filename):
    return send_from_directory(filename, static_url_path='static')

if __name__ == '__main__':
    app.run(*host, debug=debug, port=port)
