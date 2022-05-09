from sqlalchemy import or_
from ....utils.build_handled_query import build_handled_query
from ... import Country


def find_many_city_query(City, query_params):
    search = query_params.get('search')
    country = query_params.get('country')
    population = query_params.get('population')
    capital_of = query_params.get('capitalof')

    queries = []

    if search:
        # Filters for matches of search term
        match = f'%{search}%'

        queries.append(or_(
            City.name.ilike(match),
            City.country_code.ilike(match),
            City.district.ilike(match)
        ))


    # Filters for records that match specific query params
    params = ['name', 'district']
    for p in params:
        param_val = query_params.get(p)

        if param_val:
            attr = getattr(City, p)
            queries.append(attr.ilike(f'%{param_val}%'))


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

    filtered_cities = City.query.filter(*queries)

    return filtered_cities


find_many = build_handled_query(find_many_city_query)
