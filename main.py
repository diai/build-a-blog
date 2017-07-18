#!/usr/bin/env python

__author__ = "student"
__version__ = "1.0"
# July 2017
# Flask Blog App Continued re: LaunchCode
# Rubric: _Project rubric_: http://education.launchcode.org/web-fundamentals/assignments/build-a-blog/


from flask import request, redirect, render_template, flash
from models import Blog
from app import app, db


@app.route('/')
def index():
    return redirect('/blog')


@app.route('/blog', methods=['GET'])
def view_blog():

    if request.args:
        post_id = request.args.get('id')
        blog = Blog.query.get(post_id)
        return render_template('one_post.html', blog=blog)

    blogs = Blog.query.order_by(Blog.date.desc()).all()
    return render_template('blog.html', blogs=blogs)


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():

    if request.method == 'POST':
        blog_title = request.form['title']
        blog_body = request.form['body']

        if not blog_title:
            flash('Please enter a blog title', 'error')
        elif not blog_body:
            flash('Please enter some blog content', 'error')
        else:
            new_blog = Blog(blog_title, blog_body)
            db.session.add(new_blog)
            db.session.commit()

            blog_id = new_blog.id
            return redirect('/blog?id=' + str(blog_id))

    return render_template('new_post.html')


if __name__ == '__main__':
    app.run()
