from flask import request
from flask_restful import Resource
from ..models import City, cities_schema, db, Country


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
