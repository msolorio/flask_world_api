from ....utils.build_handled_query import build_handled_query
from ....utils.has_all_required_fields import has_all_required_fields
from ... import ClientError

from ... import db

def create_city_query(City, city_data):

    required_fields = (
        'name',
        'country_code',
        'district',
        'population'
    )

    valid, missing_fields = has_all_required_fields(city_data, required_fields)

    if not valid:
        return ClientError(f'Missing fields: {missing_fields}', 400)

    new_city = City(
        name=city_data['name'],
        country_code=city_data['country_code'],
        district=city_data['district'],
        population=city_data['population']
    )

    db.session.add(new_city)
    db.session.commit()


    return new_city

create = build_handled_query(create_city_query)
