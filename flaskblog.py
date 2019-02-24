#!/usr/bin/env python
# coding: utf-8
# @Auther: Brandon Rickman
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
		'author':'Brandon Rickman',
		'title':'Blog Post One',
		'content':'First post content.',
		'post_date':'February 24, 2019'
	},
	{
		'author':'Jane Doe',
		'title':'Blog Post Two',
		'content':'Second post content.',
		'post_date':'February 25, 2019'
	},
	{
		'author':'John Doe',
		'title':'Blog Post Three',
		'content':'Third blog post content.',
		'post_date':'February 26, 2019'
	}
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts = posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
	app.run(debug=True)




