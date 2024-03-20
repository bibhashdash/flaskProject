from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import unittest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    error_deleting_task = 'There was an error deleting this task'

    def __repr__(self):
        return '<Task %r>' % self.id


with app.app_context():
    db.create_all()


class Bike:
    quantity = 0

    def __init__(self, make: str, model: str, frame_size: int):
        self.make = make
        self.model = model
        self.frame_size = frame_size
        Bike.quantity += 1

    def __del__(self):
        Bike.quantity -= 1

    def __str__(self):
        return "Your bike is a {} {} of Frame Size {}".format(self.make, self.model, self.frame_size)


class RoadBikes(Bike):

    def __init__(self, make, model, frame_size, has_disc_brake: bool):
        super().__init__(make, model, frame_size)
        self.has_disc_brake = has_disc_brake

    def __str__(self):
        text = super().__str__()
        if self.has_disc_brake:
            text += ", and it has disc brakes"
        else:
            text += ", and it does not have disc brakes"
        return text


bibhash_bike = RoadBikes("Scott", "Speedster", 54, False)
print(bibhash_bike)


class BallVector:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other):
        vector_difference = BallVector(self.x - other.x, self.y - other.y)
        return vector_difference


vector1 = BallVector(3, 5)
vector2 = BallVector(1, 2)
print(vector2 - vector1)


@app.route('/', methods=['POST', 'GET'])
def index():  # put application's code here
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except RuntimeError as e:
            return str(e)
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(taskid):
    task_to_delete = Todo.query.get_or_404(taskid)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
    except RuntimeError as e:
        return str(e)
    finally:
        return redirect('/')


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(taskid):
    task_to_update = Todo.query.get_or_404(taskid)
    if request.method == 'POST':
        updated_content = request.form['content']
        task_to_update.content = updated_content
        try:
            db.session.commit()
            return redirect('/')
        except RuntimeError as e:
            return str(e)
    else:
        return render_template('update.html', task=task_to_update)


# if __name__ == '__main__':
#     app.run(debug=True)
