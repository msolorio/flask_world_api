from . import db, ma

class Country(db.Model):
    __tablename__ = 'countries'

    code = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String(127), nullable=False)
    continent = db.Column(db.String(127), nullable=False)
    region = db.Column(db.String(127), nullable=False)
    surfacearea = db.Column(db.Integer, nullable=False)
    indepyear = db.Column(db.Integer)
    population = db.Column(db.Integer, nullable=False)
    lifeexpectancy = db.Column(db.Float)
    gnp = db.Column(db.Float)
    gnpold = db.Column(db.Float)
    localname = db.Column(db.String(127), nullable=False)
    governmentform = db.Column(db.String(127), nullable=False)
    headofstate = db.Column(db.String(127))
    capital_id = db.Column(db.Integer)
    code2 = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return f'<Country code={self.code}>'



class CountrySchema(ma.Schema):
    class Meta:
        fields = ('code', 'name', 'continent', 'region', 'surfacearea', 'indepyear', 'population', 'lifeexpectancy', 'localname', 'governmentform', 'capital_id')
        model = Country

    cities = ma.Nested('CitySchema', many=True, exclude=('country',))
    capital = ma.Nested('CitySchema', exclude=('country',))


class CountryReducedSchema(ma.Schema):
    class Meta:
        fields = ('code', 'name')
        model: Country


country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)

country_reduced_schema = CountryReducedSchema()
