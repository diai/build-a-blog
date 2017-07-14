from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
# Note: the connection string after :// contains the following info:
# user:password@server:portNumber/databaseName

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:123456789@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(10000))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/', methods=['POST', 'GET'])
def index():
    form_value = request.args.get('id')
    if (form_value == None):
        blogs = Blog.query.all()
        return render_template('blog.html', 
            blogs=blogs)
    else:
        return redirect('/blog?id='+form_value)

@app.route('/blog', methods=['GET'])
def view_blog():
    form_value = int(request.args.get('id'))
    blogs = Blog.query.filter_by(id = form_value).all()
    return render_template('newpost.html', blogs = blogs)

@app.route('/addpost', methods=['POST', 'GET'])
def addpost():
    if request.method == 'POST':
        blog_title = request.form['blog_title']
        blog_body = request.form['blog_content']
        
        title_error = ''
        content_error = ''

        if (blog_title == ''):
            title_error = 'Please enter a blog title'
        if (blog_body == ''):
            content_error = 'Please enter some blog content'

        if (title_error != '' or content_error != ''):
            return render_template('addpost.html',title = blog_title, content = blog_body, title_error = title_error, content_error = content_error)
        else:
            new_blog = Blog(blog_title, blog_body)
            db.session.add(new_blog)
            db.session.commit()
            blog_id = new_blog.id
            return redirect('/blog?id='+str(blog_id))
    
    if request.method == 'GET':
        return render_template('addpost.html')


if __name__ == '__main__':
    app.run()