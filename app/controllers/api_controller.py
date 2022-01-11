from flask_restful import Resource

class ApiResource(Resource):
    def get(self):
        return { 'message': 'Welcome to the World Data API. Navigate to /api/docs to access OpenAPI docs.' }


# TODO: Add /api/docs Open API resource and route here