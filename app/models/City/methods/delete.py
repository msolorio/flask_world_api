from ....utils.build_handled_query import build_handled_query
from ... import db
from ... import ClientError


def delete_city_query(City, city_id):
    city = City.query.get(city_id)

    if not city:
        return ClientError('A city with that id does not exist.')

    db.session.delete(city)
    db.session.commit()


delete = build_handled_query(delete_city_query)
