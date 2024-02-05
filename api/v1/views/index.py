#!/usr/bin/python3
"""index view"""
from api.v1.views import app_views
from flask import Flask, jsonify, Blueprint
from models import storage


objects = {
    "states": "State",
    "cities": "City",
    "places": "Place",
    "amenities": "Amenity",
    "users": "User",
    "reviews": "Review"
}


@app_views.route('/status')
def app_status():
    """application status"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats')
def app_stats():
    """application stats"""
    number_objs = {}
    for k, v in objects.items():
        number_objs[k] = storage.count(v)
    return jsonify(number_objs)

if __name__ == "__main__":
    pass
