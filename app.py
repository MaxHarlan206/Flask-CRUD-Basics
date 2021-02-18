from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World, this is Max Harlan!'

@app.route('/search_results')
def search_results():
    return 'Pretty neat search page'