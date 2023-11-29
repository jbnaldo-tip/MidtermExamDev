from flask import Flask, jsonify, request
app = Flask(__name__)
Informations = [
    {
        "heart_id": "1",
        "date": ["Aug 1, 2000"],
        "heart_rate": ["100/60"]
    },
    {
        "heart_id": "2",
        "date": ["Nov 23, 2005"],
        "heart_rate": ["120/80"]
    }
]
@app.route('/Informations', methods=['GET'])
def getInformations():
    return jsonify(informations)

@app.route('/Informations', methods=['POST'])
def add_information():
    information = request.get_json()
    informations.append(informations)
    return {'id': len(informations)}, 200

if __name__=='__main__':
    app.run()