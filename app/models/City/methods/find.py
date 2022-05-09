from ....utils.build_handled_query import build_handled_query
from ... import ClientError

from ... import db


def find_city_query(City, city_id):
    found_city = City.query.get(city_id)

    if not found_city:
        return ClientError('No city found with that id.', 404)

    return found_city


find = build_handled_query(find_city_query)
