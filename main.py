 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutors.db'
db = SQLAlchemy(app)

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    subjects = db.Column(db.String(255), nullable=False)
    availability = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Tutor %r>' % self.name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tutors')
def tutors():
    tutors = Tutor.query.all()
    return render_template('tutors.html', tutors=tutors)

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
