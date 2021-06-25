from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Contact': u'987653410',
        'Name': u'Raju', 
        'done': False
    },
    {
        'id': 2,
        'Contact': u'7981123563',
        'Name': u'Rahul', 
        'done': False
    },
    {
        'id': 3,
        'Contact': u'6300978120',
        'Name': u'Rajesh', 
        'done': False
    },
    {
        'id': 4,
        'Contact': u'7924025186',
        'Name': u'Ramu', 
        'done': False
    },{
        'id': 5,
        'Contact': u'7406474563',
        'Name': u'Ram', 
        'done': False
    },
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please enter the contact!"
        },400)

    contact_list = {
        'id': contacts[-1]['id'] + 1,
        'Contact': request.json['Contact'],
        'Name': request.json.get('Name', ""),
        'done': False
    }
    contacts.append(contact_list)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)