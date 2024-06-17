import warnings

import subprocess

import db

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app)

items = []

@app.route('/api/etudiant', methods=['GET'])
def get_etudiants():
    db.getetudiants()
    result = db.resultsExportEtudiants
    print(result)
    return jsonify({'item': result}), 201


@app.route('/api/etudiant', methods=['POST'])
def create_etudiant():
    db.createetudiant(request.json)

    return jsonify({'item': 'etudiant cree'}), 201


if __name__ == '__main__':
    app.run(debug=True)