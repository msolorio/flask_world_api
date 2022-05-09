from ....utils.build_handled_query import build_handled_query
from ... import ClientError
from ... import db


def update_city_query(City, city_id, provided_fields):
    city = City.query.get(city_id)
    
    if not city:
        return ClientError('No city found with that id.', 404)

    available_fields = (
        'name',
        'country_code',
        'district',
        'population'
    )

    for key, value in provided_fields:
        if key in available_fields:
            setattr(city, key, value)

    db.session.commit()

    updated_city = city

    return updated_city


update = build_handled_query(update_city_query)
