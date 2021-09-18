from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [
    {
        "Contact":u"9987644456",
        "Name":u"Raju",
        "done":False,
        "id":1
    },
    {
        "Contact":u"9876543222",
        "Name":u"Rahul",
        "done":False,
        "id":2
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods = ["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide the data!!"
        },400)
    
    contact = {
        'id': contacts [-1] ["id"] + 1,
        'Name': request.json ["Name"],
        'Contact': request.json.get('Contact',""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status": "Success",
        "message": "Task Added Successfully"

    })

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data": contacts
    })


if(__name__=="__main__"):
    app.run(debug=True)