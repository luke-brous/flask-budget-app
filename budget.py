from flask import Flask, render_template, redirect, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)

@app.route('/')
def home():
    # Example data to pass to the template
    title = "Budget App"
    description = "Track your expenses and manage your budget effectively."
    return render_template('index.html', title=title, description=description)

if __name__ == '__main__':
    app.run(debug=True)
