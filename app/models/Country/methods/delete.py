from ... import db

def delete(Country, countrycode):
    country = Country.query.get(countrycode)

    db.session.delete(country)
    db.session.commit()    
