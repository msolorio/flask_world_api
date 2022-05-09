from ....utils.build_handled_query import build_handled_query
from ... import ClientError
from ... import db


def update_country_query(Country, country_code, provided_fields):
    country = Country.query.get(country_code)

    if not country:
        return ClientError('No country found with that country code.', 404)

    available_fields = (
        'name',
        'continent',
        'region',
        'surfacearea',
        'indepyear',
        'population',
        'lifeexpectancy',
        'localname',
        'governmentform',
        'capital_id',
        'code2'
    )

    for key, value in provided_fields:
        if key in available_fields:
            setattr(country, key, value)

    db.session.commit()

    updated_country = country

    return updated_country


update = build_handled_query(update_country_query)
