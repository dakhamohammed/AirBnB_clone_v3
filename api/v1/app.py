#!/usr/bin/python3
"""Status of our API"""
from models import storage
from flask import Flask, make_response, jsonify
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(code):
    """calls storage.close() on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handler for 404 error page"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')),
            threaded=True)
