from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_results')
def search_results():
    return 'Pretty neat search page'

if __name__ == '__main__':
    app.run(debug = True)