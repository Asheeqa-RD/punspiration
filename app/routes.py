import json
from flask import Blueprint,jsonify

from app.utils import format_response

main_bp=Blueprint('main',__name__)

@main_bp.route('/')
def home():
    
    return jsonify({"message": "Welcome to Punspiration!"})

with open('puns/puns.json') as f:
    PUNS =json.load(f)
    
@main_bp.route('/puns/<category>') 
def get_puns_by_category(category):
    filtered_puns=[pun for pun in PUNS if pun['category']== category]
    if not filtered_puns :
        return jsonify(format_response("error","No puns found in this category")), 404
    
    return jsonify(format_response("success","Puns for category :{category}",filtered_puns)),999
    
    
    
    
    