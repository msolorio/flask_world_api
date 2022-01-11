from flask import request
from flask_restful import Resource
from ..models import City, cities_schema, city_schema, db, Country
from ..utils.has_all_required_fields import has_all_required_fields


class CitiesResource(Resource):
    def get(self):
        queries = []
        country = request.args.get('country')
        population = request.args.get('population')
        capital_of = request.args.get('capital_of')

        if country:
            # query cities with a country with name matching query param
            match = f'%{country}%'
            queries.append(City.country.has(Country.name.ilike(match)))


        if population:
            # filters for records with population greater/less than query param
            members = population.split(':')
            direction = members[0]
            num_val = int(members[1])

            if direction == 'gt':
                queries.append(City.population > num_val)
            if direction == 'lt':
                queries.append(City.population < num_val)


        if capital_of:
            # Get city with id that matches capital_id of country passed in param
            match = f'%{capital_of}%'
            queries.append(City.id == Country.query.filter(Country.name.ilike(match))[0].capital_id)

        cities = City.query.filter(*queries)
        cities_json = cities_schema.dump(cities)

        return {
            '_length': len(cities_json),
            'cities': cities_json
        }


    def post(self):
        req_data = request.get_json()

        required_fields = (
            'name',
            'countrycode',
            'district',
            'population'
        )

        valid, fields = has_all_required_fields(req_data, required_fields)

        if not valid:
            return { 'message': f'Missing fields: {fields}' }

        new_city = City(
            name=req_data['name'],
            countrycode=req_data['countrycode'],
            district=req_data['district'],
            population=req_data['population']
        )

        db.session.add(new_city)
        db.session.commit()

        return city_schema.dump(new_city)


class CityResource(Resource):
    def get(self, city_id):
        city = City.query.get(city_id)

        if not city:
            return { 'message': 'No city found with that id.' }, 404

        return city_schema.dump(city), 200
