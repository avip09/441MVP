import os
import pathlib
import uuid
import hashlib
import flask
import arrow
from flask import session, redirect, request
import foodapp

@foodapp.app.route('/grouphome/')
def change_password():
    return flask.render_template("password.html")

@foodapp.app.route('/groups/', methods=['POST'])
def logout_account():
    if flask.request.form['operation'] == 'Create Group':
        return flask.render_template("creategroup.html")
    else:
        return flask.render_template("joingroup.html")