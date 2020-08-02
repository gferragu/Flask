from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy # Note, the 'SQAL' portion ***needs*** to be capitalized
from datetime import datetime

# To run in new terminal:
#/opt/anaconda3/envs/flask/bin/python /Users/gabriel/Documents/Web_dev/Flask/task_master_tutorial/app.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class to_do(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    