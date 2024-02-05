#!/usr/bin/python3
"""index view"""
from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route('/status')
def app_status():
    """app status"""
    return jsonify({"status": "OK"})
