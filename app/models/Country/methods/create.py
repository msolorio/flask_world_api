from ... import db

def create(Country, country_data):
    new_country = Country(**country_data)

    if not new_country:
        return { 'message': 'Invalid input' }

    db.session.add(new_country)
    db.session.commit()

    return new_country
