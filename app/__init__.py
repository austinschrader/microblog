# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:09:47 2020

@author: austin.schrader
"""

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes