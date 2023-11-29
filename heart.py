from flask import Flask, jsonify, request
app = Flask(__name__)
records = [
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
@app.route('/Records', methods=['GET'])
def getRecords():
    return jsonify(records)

@app.route('/Records', methods=['POST'])
def add_record():
    record = request.get_json()
    records.append(records)
    return {'id': len(records)}, 200

if __name__=='__main__':
    app.run()