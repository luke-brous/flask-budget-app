from flask import Flask, render_template, redirect, url_for
from flask_mysqldb import MySQL

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'brouslr0' or 'burtar0'
app.config['MYSQL_PASSWORD'] = 'penis' or 'balls'
app.config['MYSQL_DB'] = 'budget_db'

mysql = MySQL(app)



@app.route('/')
def home():
    # Example data to pass to the template
    
    title = "Budget App"
    resources = "Resources"
    create_budget = "Budget"
    summary = "Summary"
    description = "Track your expenses and manage your budget effectively, all in one place."
    return render_template('index.html', title=title, description=description)

if __name__ == '__main__':
    app.run(debug=True)
