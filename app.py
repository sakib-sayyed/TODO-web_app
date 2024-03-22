from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')


class TODO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now(IST))
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

@app.route('/')
def index():
    todos = TODO.query.all()
    return render_template('base.html', todo_list=todos)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        todo = TODO(title=title, description=description)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('base.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    todo = TODO.query.get(id)
    if request.method == 'POST':
        todo.title = request.form.get('title')
        todo.description = request.form.get('description')
        db.session.commit()
        return redirect('/')
    return render_template('base.html', todo=todo)

@app.route('/delete/<int:id>')
def delete(id):
    todo = TODO.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route('/complete/<int:id>')
def complete_task(id):
    todo = TODO.query.get(id)
    todo.completed = True
    db.session.commit()
    return redirect('/')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
