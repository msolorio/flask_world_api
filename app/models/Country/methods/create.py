from ....utils.build_handled_query import build_handled_query
from ... import ClientError

from ... import db

def create_country_query(Country, country_data):
    country_code = country_data['code']

    existing_country = Country.query.get(country_code)

    if existing_country:
        return ClientError('A country with that code already exists')

    new_country = Country(**country_data)

    db.session.add(new_country)
    db.session.commit()

    return new_country


create = build_handled_query(create_country_query)
