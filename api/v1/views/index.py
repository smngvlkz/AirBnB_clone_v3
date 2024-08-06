#!/usr/bin/python3
"""Index view for the API."""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def status():
    """Return API status."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """Retrieve the number of each object type."""
    class_mapping = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }
    
    stats_dict = {}
    for key, cls in class_mapping.items():
        count = storage.count(cls)
        stats_dict[key] = count
    
    return jsonify(stats_dict)
