import json
from flask import request
from flask_restful import Resource
from ..models import Country, country_schema, countries_schema, generalError


class CountriesResource(Resource):
    def get(self):
        query_params = request.args

        response = Country.find_many(query_params)

        if isinstance(response, generalError):
            return response.dict(), response.status

        found_countries = countries_schema.dump(response)

        return {
            '_length': len(found_countries),
            '_status': 200,
            'countries': found_countries
        }, 200




    def post(self):
        country_data = request.json

        response = Country.create(country_data)

        if isinstance(response, generalError):
            return response.dict(), response.status

        created_country = country_schema.dump(response)

        return {
            '_status': 201,
            'created_country': created_country
        }, 201



class CountryResource(Resource):
    def get(self, country_code):
        response = Country.find(country_code)

        if isinstance(response, generalError):
            return response.dict(), response.status

        found_country = country_schema.dump(response)

        return {
            '_status': 200,
            'found_country': found_country
        }, 200



    def patch(self, country_code):
        provided_fields = request.json.items()

        response = Country.update(country_code, provided_fields)

        if isinstance(response, generalError):
            return response.dict(), response.status

        updated_country = country_schema.dump(response)

        return {
            '_status': 200,
            'updated_country': updated_country
        }, 200



    def delete(self, country_code):
        response = Country.delete(country_code)

        if isinstance(response, generalError):
            return response.dict(), response.status

        return {
            '_status': 200,
            'message': 'Country deleted'
        }, 200
