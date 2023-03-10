import os
import pathlib
import uuid
import hashlib
import flask
import arrow
import random
from flask import Flask, session, redirect, request, render_template, url_for
from user import User

#from algorithms.recommendationAlgorithm import recommendationAlgorithm

app = Flask(__name__)
app.secret_key = "EECS441"

sessions = {}
current_session_id = 0

@app.route('/login/', methods = ['POST'])
def login_user():
    session['username'] = flask.request.form['username']
    return redirect(flask.url_for('group_home'))

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/group/')
def group_page():
    session_code = request.args.get('session_code', None)
    users = sessions[session_code]

    # Get names of user in session
    # TODO This should update client side
    names = []
    for user in users:
        names.append(user.getName())

    return render_template('group.html', session_code=session_code, names=names)

@app.route('/grouphome/', methods = ['GET', 'POST'])
def group_home():
    global current_session_id
    if request.method == 'POST':
        operation = request.form.get('operation')

        new_user = User(session['username'])

        if operation == "create":
            # Create new group session
            session_code = str(current_session_id)
            current_session_id = current_session_id + 1

            # Add user to new session
            sessions[session_code] = [new_user]
        else:
            session_code = request.form.get('session_join')
            
            # Add user to session
            sessions[session_code].append(new_user)

        session["session_code"] = session_code

        users = sessions[session_code]

        return redirect(url_for('group_page', session_code=session_code))
    return render_template('grouphome.html')

@app.route('/preference/')
def preference_page():
    return render_template('preference.html')