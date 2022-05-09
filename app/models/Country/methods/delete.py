from ....utils.build_handled_query import build_handled_query
from ... import db
from ... import ClientError


def delete_country_query(Country, countrycode):
    country = Country.query.get(countrycode)

    if not country:
        return ClientError('A country with that countrycode does not exist.')

    db.session.delete(country)
    db.session.commit()    


delete = build_handled_query(delete_country_query)
