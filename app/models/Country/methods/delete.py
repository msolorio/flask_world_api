from ....utils.build_handled_query import build_handled_query
from ... import db
from ... import ClientError


def delete_country_query(Country, country_code):
    country = Country.query.get(country_code)

    if not country:
        return ClientError('A country with that country_code does not exist.')

    db.session.delete(country)
    db.session.commit()    


delete = build_handled_query(delete_country_query)
