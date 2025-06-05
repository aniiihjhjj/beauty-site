from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visao')
def visao():
    return render_template('visao.html')

@app.route('/valores')
def valores():
    return render_template('valores.html')

@app.route('/interesse')
def interesse():
    return render_template('interesse.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)