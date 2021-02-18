from flask import Flask, render_template

app = Flask(__name__)
all_posts = [
    {
       'title': 'post1',
       'content': 'this is the content of post 1',
        'author': 'Max Harlan'
    },
    {
        'title': 'post2',
        'content': 'this is the content of post 2'
    }
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/search_results')
def search_results():
    return 'Pretty neat search page'

if __name__ == '__main__':
    app.run(debug = True)