from flask import Blueprint
from .controllers.countriesController import countries_bp

api_bp = Blueprint('api_bp', __name__)

api_bp.register_blueprint(countries_bp, url_prefix='/countries')

@api_bp.route('/')
def api_root():
    return { 'message': 'Welcome to the World Data API. Navigate to /api/docs to access OpenAPI docs.' }

# TODO: add route for open api docs