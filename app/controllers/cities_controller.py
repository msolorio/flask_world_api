from flask import request
from flask_restful import Resource
from ..models import City, cities_schema, city_schema, Country, generalError


class CitiesResource(Resource):
    def get(self):
        query_params = request.args

        response = City.find_many(query_params)

        if isinstance(response, generalError):
            return response.dict(), response.status        
        
        found_cities = cities_schema.dump(response)

        return {
            '_status': 200,
            '_length': len(found_cities),
            'cities': found_cities
        }


    def post(self):
        city_data = request.get_json()

        response = City.create(city_data)

        if isinstance(response, generalError):
            return response.dict(), response.status        

        created_city = city_schema.dump(response)

        return {
            '_status': 201,
            'created_city': created_city
        }, 201


class CityResource(Resource):
    def get(self, city_id):
        response = City.find(city_id)

        if isinstance(response, generalError):
            return response.dict(), response.status

        found_city = city_schema.dump(response)

        return {
            '_status': 200,
            'found_city': found_city
        }, 200



    def patch(self, city_id):
        provided_fields = request.json.items()

        response = City.update(city_id, provided_fields)

        if isinstance(response, generalError):
            return response.dict(), response.status

        updated_city = city_schema.dump(response)

        return {
            '_status': 200,
            'updated_city': updated_city
        }, 200



    def delete(self, city_id):
        response = City.delete(city_id)

        if isinstance(response, generalError):
            return response.dict(), response.status

        return {
            '_status': 200,
            'message': 'City deleted'
        }, 200
