<<<<<<< HEAD
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/student-details', methods=['GET'])
def get_details():
    return jsonify({
        "name": "Shalini",
        "roll": "2023bcs00229",
        "register": "bcs229"
    })

if __name__ == '__main__':
=======
from flask import Flask, jsonify
from flask_cors import CORS   # ADD THIS

app = Flask(__name__)
CORS(app)   # ADD THIS

@app.route('/student-details', methods=['GET'])
def get_details():
    return jsonify({
        "name": "Shalini",
        "roll": "2023bcs00229",
        "register": "bcs229"
    })

if __name__ == '__main__':
>>>>>>> d8f3121 (Initial project commit)
    app.run(host='0.0.0.0', port=5000)