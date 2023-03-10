import os
import pathlib
import uuid
import hashlib
import flask
import arrow
from flask import Flask, session, redirect, request, render_template

app = Flask(__name__)

@app.route('/grouphome/')
def change_password():
    return flask.render_template("grouphome.html")

@app.route('/groups/', methods=['POST'])
def logout_account():
    if flask.request.form['operation'] == 'Create Group':
        return flask.render_template("creategroup.html")
    else:
        return flask.render_template("joingroup.html")