import json
from flask import request
from flask_restful import Resource
from sqlalchemy import or_
from ..models import Country, country_schema, countries_schema, db, generalError


class CountriesResource(Resource):
    def get(self):
        query_params = request.args

        response = Country.find_many(query_params)

        if isinstance(response, generalError):
            return response.dict(), response.status

        countries_json = countries_schema.dump(response)

        return {
            '_length': len(countries_json),
            'countries': countries_json
        }, 200




    def post(self):
        country_data = request.json

        response = Country.create(country_data)

        if isinstance(response, generalError):
            return response.dict(), response.status

        return country_schema.dump(response), 201



class CountryResource(Resource):
    def get(self, countrycode):
        response = Country.find(countrycode)

        if isinstance(response, generalError):
            return response.dict(), response.status

        return country_schema.dump(response), 200



    def patch(self, countrycode):
        provided_fields = request.json.items()

        response = Country.update(countrycode, provided_fields)

        if isinstance(response, generalError):
            return response.dict(), response.status

        return country_schema.dump(response), 200



    def delete(self, countrycode):
        response = Country.delete(countrycode)

        if isinstance(response, generalError):
            return response.dict(), response.status

        return {
            'success': True,
            'message': 'Country deleted'
        }, 200
