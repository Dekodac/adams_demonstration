from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class Student:
    """student"""
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')

all_students = []
# Add some students
all_students.append(Student({'id': 1, 'name': 'Harry'}))
all_students.append(Student({'id': 2, 'name': 'Hermione'}))
all_students.append(Student({'id': 2, 'name': 'Ron'}))

@app.route('/', methods=['GET'])
def base_route():
    return "ping"

@app.route('/students', methods=['GET'])
def get_students():
    """get all students"""
    student_list = [
        {'id': student.id, 'name': student.name}
        for student in all_students
    ]
    return jsonify(student_list)

app.run(debug=True)