import os
import pathlib
import uuid
import hashlib
import flask
import arrow
import random
from flask import Flask, session, redirect, request, render_template, url_for

#from algorithms.recommendationAlgorithm import recommendationAlgorithm

app = Flask(__name__)

sessions = {}
current_session_id = 0

@app.route('/login/', methods = ['POST'])
def login_user():
    session['username'] = flask.request.form['username']
    return redirect(flask.url_for('show_index'))


def index_page():
    return render_template('index.html')

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/group/')
def group_page():
    session_code = request.args.get('session_code', None)
    group = request.args.getlist('group')
    return render_template('group.html', session_code=session_code, group=group)

@app.route('/grouphome/', methods = ['GET', 'POST'])
def group_home():
    global current_session_id
    if request.method == 'POST':
        operation = request.form.get('operation')

        if operation == "create":
            session_code = str(current_session_id)
            current_session_id = current_session_id + 1

            sessions[session_code] = ["Chad"]
        else:
            session_code = request.form.get('session_join')
            
            sessions[session_code].append("Avi")

        group = sessions[session_code]

        return redirect(url_for('group_page', session_code=session_code, group=group))
    return render_template('grouphome.html')

# @app.route('/groups/')
# def logout_account():
#     if flask.request.form['operation'] == 'Create Group':
#         return flask.render_template("creategroup.html")
#     else:
#         return flask.render_template("joingroup.html")

@app.route('/preference')
def preference_page():
    return render_template('preference.html')