from flask import request
from flask_restful import Resource
from sqlalchemy import or_
from ..models import Country, country_schema, countries_schema, db, generalError


class CountriesResource(Resource):
    def get(self):
        queries = []
        search = request.args.get('search')

        # Filters for matches of search term
        if search:
            match = f'%{search}%'

            queries.append(or_(
                Country.code.ilike(match),
                Country.name.ilike(match),
                Country.continent.ilike(match),
                Country.region.ilike(match),
                Country.localname.ilike(match),
                Country.governmentform.ilike(match)
            ))


        # Filters for records that match specific query params
        params = ['name', 'continent', 'governmentform']
        for p in params:
            param_val = request.args.get(p)

            if param_val:
                attr = getattr(Country, p)
                queries.append(attr.ilike(f'%{param_val}%'))


        # filters for records with numeric values greater/less than query param values
        num_params = ['population', 'lifeexpectancy', 'surfacearea']
        for p in num_params:
            param_val = request.args.get(p)

            if param_val:
                attr = getattr(Country, p)
                members = param_val.split(':')
                direction = members[0]
                num_val = int(members[1])

                if direction == 'gt':
                    queries.append(attr > num_val)
                if direction == 'lt':
                    queries.append(attr < num_val)


        countries = Country.query.filter(*queries)

        countries_json = countries_schema.dump(countries)

        return {
            '_length': len(countries_json),
            'countries': countries_json
        }, 200



    def post(self):
        country_data = request.json

        response = Country.create(country_data)

        if isinstance(response, generalError):
            return response.message, response.status

        return country_schema.dump(response), 201



class CountryResource(Resource):
    def get(self, countrycode):
        country = Country.query.get(countrycode)

        if not country:
            return { 'message': 'No country found with that countrycode.' }, 404

        return country_schema.dump(country), 200


    def patch(self, countrycode):
        country = Country.query.get(countrycode)

        if not country:
            return { 'message': 'No country found with that countrycode.' }, 404

        available_fields = (
            'name',
            'continent',
            'region',
            'surfacearea',
            'indepyear',
            'population',
            'lifeexpectancy',
            'localname',
            'governmentform',
            'capital_id',
            'code2'
        )

        for key, value in request.json.items():
            if key in available_fields:
                setattr(country, key, value)

        db.session.commit()

        return country_schema.dump(country), 200


    def delete(self, countrycode):
        Country.delete(countrycode)

        return { 'message': 'Country deleted' }, 200