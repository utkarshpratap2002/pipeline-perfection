from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    mydetails = {
        "name": "Utkarsh Pratap Singh",
        "rollno": 86921,
        "PNR": 240844223055
    
    return mydetails

app.run(host="0.0.0.0", port=4000)
