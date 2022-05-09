from sqlalchemy import or_
from ....utils.build_handled_query import build_handled_query
from ... import ClientError

def find_many_country_query(Country, query_params):

    queries = []

    # Filters for matches of search term
    search = query_params.get('search')

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
        param_val = query_params.get(p)

        if param_val:
            attr = getattr(Country, p)
            queries.append(attr.ilike(f'%{param_val}%'))


    # filters for records with numeric values greater/less than query param value
    num_params = ['population', 'lifeexpectancy', 'surfacearea']
    for p in num_params:
        param_val = query_params.get(p)

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

    return countries


find_many = build_handled_query(find_many_country_query)
