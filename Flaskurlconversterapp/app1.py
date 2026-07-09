from flask import Flask, request, jsonify

app=Flask(__name__)

students = [{'id': 1, 'name': 'Charan', 'marks': 80},{'id': 2, 'name': 'Sai', 'marks': 82}]


@app.route('/AddStudent',methods=['GET','POST'])
def AddStudent():
    global students

    if request.method == 'GET':
        return jsonify({
            "students": students
        }),200
    
    if request.method == 'POST':
        data = request.get_json()
        id = data['id']
        name = data['name']
        marks = data['marks']
        for student in students:
            if student['id'] == id:
                return jsonify({"message":f"Student already exits"}),200
        students.append(
        {
            'id': id, 
            'name': name,
            'marks': marks
        })
        return jsonify({
            "message":"student added successfully",
            "data":students
        })

@app.route('/UpdateStudent/<int:id>',methods=['PUT'])
def UpdateStudent(id):
    global students
    data = request.get_json()
    marks = data['marks']
    for student in students:
        if student['id']==id:
            student['marks'] = marks
            return jsonify({"message":f"Student id {id} marks is updated","updated data is ": student}),200
    return jsonify({"message":f"Student id {id} not found"}),404


@app.route('/DeleteStudent/<int:id>',methods=['DELETE'])
def DeleteStudent(id):
    global students
    for student in students:
        if student['id']== id:
            students.remove(student)
            return jsonify({"message":f"Student id {id} is deleted successfully","updated data is ": students}),200
    return jsonify({"message":f"Student id {id} not found"}),404
    
app.run(debug=True)
