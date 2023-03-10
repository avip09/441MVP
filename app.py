import os
import pathlib
import uuid
import hashlib
import flask
import arrow
import random
from flask import Flask, session, redirect, request, render_template, url_for
from user import User

from algorithms.recommendationAlgorithm import Recommender

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
    global sessions
    session_code = request.args.get('session_code', None)
    users = sessions[session_code]

    # Get names of user in session
    # TODO This should update client side
    names = []
    for user in users:
        names.append(user)

    return render_template('group.html', session_code=session_code, names=names)

@app.route('/grouphome/', methods = ['GET', 'POST'])
def group_home():
    global current_session_id, sessions
    if request.method == 'POST':
        operation = request.form.get('operation')

        new_user = User(session['username'])

        if operation == "create":
            # Create new group session
            session_code = str(current_session_id)
            current_session_id = current_session_id + 1

            # Add user to new session
            sessions[session_code] = {session['username'] : new_user}
        else:
            session_code = request.form.get('session_join')
            
            # Add user to session
            sessions[session_code][session['username']] = new_user

        session["session_code"] = session_code

        users = sessions[session_code]

        return redirect(url_for('group_page', session_code=session_code))
    return render_template('grouphome.html')

@app.route('/preference/', methods = ['GET', 'POST'])
def preference_page():
    global sessions
    if request.method == 'POST':
        option1 = request.form.get('option1')
        option2 = request.form.get('option2')
        option3 = request.form.get('option3')

        sessions[session['session_code']][session['username']].setPref(option1, option2, option3)

        allSet = True
        for username in sessions[session['session_code']].keys():
            if not sessions[session['session_code']][username].isPrefSet():
                allSet = False

        if allSet:
            rec = Recommender(len(sessions[session['session_code']]))
            
            for username in sessions[session['session_code']]:
                rec.addUserPreferences(sessions[session['session_code']][username].getCuisines(), 1, 4)

            return render_template('results.html', results=rec.getPreferences())
        else:
            return render_template('waiting.html')
    
    return render_template('preference.html')