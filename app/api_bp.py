from flask import Blueprint

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/')
def api_root():
    return { 'message': 'Welcome to the World Data API. Navigate to /api/docs to access OpenAPI docs.' }

# TODO: add route for open api docs