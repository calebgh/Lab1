from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
  data = json.load(f)


@app.route('/')
def hello_world():
  return 'Hello, World!'  # return 'Hello World' in response


@app.route('/students')
def get_students():
  return jsonify(data)  # return student data in response


@app.route('/hello/<string:a>/<string:b>')
def hello_name(a, b):
  return 'Hi ' + a + ' ' + b + '!'


@app.route('/studentss')
def get_studentss():
  result = []
  pref = request.args.get('pref')  # get the parameter from url
  if pref:
    for student in data:  # iterate dataset
      if student[
          'pref'] == pref:  # select only the students with a given meal preference
        result.append(student)  # add match student to the result
    return jsonify(result)  # return filtered set if parameter is supplied
  return jsonify(data)


@app.route('/students/<id>')
def get_student(id):
  for student in data:
    if student['id'] == id:  # filter out the students without the specified id
      return jsonify(student)


@app.route('/stats')
def get_stats():

  chicken = 0
  fish = 0
  csm = 0
  css = 0
  itm = 0
  its = 0
  vege = 0

  for student in data:
    if student['pref'] == "Chicken":
      chicken += 1
    if student['programme'] == "Computer Science (Major)":
      csm += 1
    if student['programme'] == "Computer Science (Special)":
      css += 1
    if student['pref'] == "Fish":
      fish += 1
    if student['programme'] == "Information Technology (Major)":
      itm += 1
    if student['programme'] == "Information Technology (Special)":
      its += 1
    if student['pref'] == "Vegetable":
      vege += 1

  return jsonify({
      "Chicken": chicken,
      "Computer Science (Major)": csm,
      "Computer Science (Special)": css,
      "Fish": fish,
      "Information Technology (Major)": itm,
      "Information Technology (Special)": its,
      "Vegetable": vege
  })


@app.route('/add/<int:a>/<int:b>')
def add_num(a, b):
  return "Sum of " + str(a) + " and " + str(b) + " is " + str(a + b)


@app.route('/subtract/<int:a>/<int:b>')
def subtract_num(a, b):
  return "Subtraction of " + str(a) + " and " + str(b) + " is " + str(a - b)


@app.route('/multiply/<int:a>/<int:b>')
def multiply_num(a, b):
  return "Multiplication of " + str(a) + " and " + str(b) + " is " + str(a * b)


@app.route('/divide/<int:a>/<int:b>')
def divide_num(a, b):
  return "Division of " + str(a) + " and " + str(b) + " is " + str(a / b)


app.run(host='0.0.0.0', port=8080, debug=True)
