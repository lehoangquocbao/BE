from flask import Flask, request, jsonify

app = Flask(__name__)
appointments = []

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json
    appointments.append(data)
    return jsonify({"message": "Appointment created"}), 201

@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify(appointments), 200

if __name__ == '__main__':
    app.run(debug=True)

