import os
from flask import Flask, redirect
from flask_migrate import Migrate
from flask_restful import Api
from .models import db, ma
from .controllers import CountriesResource, CountryResource, CitiesResource, CityResource, ApiResource, DocsResource

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    db.init_app(app)
    ma.init_app(app)
    api = Api(app, '/api')
    Migrate(app, db)

    api.add_resource(ApiResource, '/')
    api.add_resource(DocsResource, '/docs')

    api.add_resource(CountriesResource, '/countries')
    api.add_resource(CountryResource, '/countries/<string:countrycode>')

    api.add_resource(CitiesResource, '/cities')
    api.add_resource(CityResource, '/cities/<int:city_id>')

    @app.route('/')
    def root():
        return redirect(api.url_for(ApiResource))

    return app
