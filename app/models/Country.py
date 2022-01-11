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
    # capital = db.relationship('City', backref='countries', lazy=True, uselist=False)
    # cities = db.relationship('City', backref='countries', lazy=True)


    def __repr__(self):
        return f'<Country code={self.code}>'



class CountrySchema(ma.Schema):
    class Meta:
        fields = ('id', 'code', 'name', 'continent', 'region', 'surfacearea', 'indepyear', 'population', 'lifeexpectancy', 'localname', 'governmentform', 'capital_id')
        model = Country

    cities = ma.Nested('CitySchema', many=True, exclude=('country',))
    capital = ma.Nested('CitySchema', exclude=('country',))


country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)
