from flask import Flask, render_template
app = Flask(__name__)

@app.route('/group')
def group_page():
    return render_template('group.html')