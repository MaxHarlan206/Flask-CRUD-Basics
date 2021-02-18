from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' # just by changing this one line later, we can use mysql or something like that which is more appropriate for production and enterprise
db = SQLAlchemy(app)

# this is the creation of a model, yes, you need to hardcode it, but is this such a big deal compared to django? no
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(40), nullable=False, default="N/A")
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post' + str(self.id)

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