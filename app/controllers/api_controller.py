from flask import render_template, make_response
from flask_restful import Resource

class ApiResource(Resource):
    def get(self):
        return { 'message': 'Welcome to the World Data API. Navigate to /api/docs to access OpenAPI docs.' }


class DocsResource(Resource):
    def get(self):
        headers = { 'Content-Type': 'text/html' }
        return make_response(render_template('openapi.html'), 200, headers)
