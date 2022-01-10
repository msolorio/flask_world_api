from . import db, ma

class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=False)
    countrycode = db.Column(db.String(3), db.ForeignKey('countries.code'), nullable=False)
    district = db.Column(db.String(127), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    country = db.relationship('Country', backref='cities', uselist=False)

    def __repr__(self):
        return f'<City id={self.id} name={self.name}>'



class CitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'countrycode', 'district', 'population')
        model = City

    country = ma.Nested('CountrySchema', excludes=('cities', 'capital'))


city_schema = CitySchema()
cities_schema = CitySchema(many=True)
