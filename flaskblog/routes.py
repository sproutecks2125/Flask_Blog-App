# coding: utf-8
# @Auther: Brandon Rickman

from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


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
def home():
    return render_template('home.html', posts = posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# FIXME: Remove this line after completion of tutorial.
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)