from flask import Blueprint, request, jsonify
from validators import validate_ethereum_address, validate_doi

api = Blueprint('api', __name__)

@api.route('/papers', methods=['POST'])
def register_paper():
    data = request.get_json()
    if not validate_ethereum_address(data.get('author_address')):
        return jsonify({"error": "Invalid Ethereum address"}), 400
    
    if not validate_doi(data.get('doi')):
        return jsonify({"error": "Invalid DOI format"}), 400
    
    # Call paper service to register paper
    return jsonify({"message": "Paper registered successfully"}), 201

@api.route('/citations', methods=['POST'])
def record_citation():
    data = request.get_json()
    if not validate_doi(data.get('citing_doi')) or not validate_doi(data.get('cited_doi')):
        return jsonify({"error": "Invalid DOI format"}), 400
    
    # Call citation service to verify and record citation
    return jsonify({"message": "Citation recorded successfully"}), 201
