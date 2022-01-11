from flask import Blueprint, request, jsonify
from sqlalchemy import or_
from ..models import Country, country_schema, countries_schema

countries_bp = Blueprint('countries', __name__)

@countries_bp.route('/<string:country_code>')
def get_country_by_code(country_code):
    country = Country.query.get(country_code)
    return country_schema.dump(country), 200


@countries_bp.route('/')
def get_countries_by_query_params():
    queries = []
    search = request.args.get('search')

    if search:
        match = f'%{search}%'

        queries.append(or_(
            Country.name.ilike(match),
            Country.continent.ilike(match),
            Country.region.ilike(match),
            Country.localname.ilike(match),
            Country.governmentform.ilike(match)
        ))

    # Loop through query params
    # if exists, creates filter for that key/value pair
    params = ['name', 'continent', 'governmentform']
    for p in params:
        param_val = request.args.get(p)

        if param_val:
            attr = getattr(Country, p)
            queries.append(attr.ilike(f'%{param_val}%'))


    # Loop through query params
    # if exists, filter for countries w/values gt or lt the param
    num_params = ['population', 'lifeexpectancy', 'surfacearea']
    for p in num_params:
        param_val = request.args.get(p)

        if param_val:
            attr = getattr(Country, p)
            members = param_val.split(':')
            num_val = int(members[1])
            direction = members[0]

            if direction == 'gt':
                queries.append(attr > num_val)
            if direction == 'lt':
                queries.append(attr < num_val)


    countries = Country.query.filter(*queries)

    return jsonify(countries_schema.dump(countries)), 200
