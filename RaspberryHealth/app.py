from flask import Flask, jsonify
from flask_cors import CORS
from SystemPerformanceLog import MenuMode

app = Flask(__name__)
CORS(app)

@app.route('/data/all', methods=['GET'])
def get_all_data():
    data = MenuMode.load_data()  # os_log_path is the path to the csv log
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)