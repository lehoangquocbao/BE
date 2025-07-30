from urllib.request import request_host

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
patients =[]
@app.route("/patients", methods=['GET'])
def get_patients():
    return jsonify(patients)

@app.route("/patients", methods=['POST'])
def add_patients():
    data= request.get_json()
    patient={
        "id":len(patients)+1,
        "name":data.get("name","anonymus"),
        "age":data.get("age","None"),
    }
    patients.append(patient)
    return jsonify(patients), 201

#start backend
if __name__ == '__main__':
    app.run(debug=True)
