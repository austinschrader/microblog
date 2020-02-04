# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:09:47 2020

@author: austin.schrader
"""

from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Austin'}
    posts = [
        {
            'author': {'username': 'Austin'},
            'body': 'We need to pay Will County'
        },
        {
            'author': {'username': 'Chris'},
            'body': 'Clark County needs a payment file'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)