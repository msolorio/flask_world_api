from ....utils.build_handled_query import build_handled_query
from ... import ClientError

from ... import db


def find_country_query(Country, country_code):
    country = Country.query.get(country_code)

    if not country:
        return ClientError('No country found with that country code.', 404)

    return country


find = build_handled_query(find_country_query)
