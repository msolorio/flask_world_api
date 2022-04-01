import os
from flask import Flask, redirect
from flask_migrate import Migrate
from flask_restful import Api
from .models import db, ma
from .controllers.countries_controller import CountriesResource, CountryResource
from .controllers.cities_controller import CitiesResource, CityResource
from .controllers.api_controller import ApiResource
from .controllers.api_controller import DocsResource
from .utils.update_database_url import update_database_url

print('in app.py')

def create_app():
    print('called create_app')

    DATABASE_URL = os.environ['DATABASE_URL']
    
    # if FLASK_ENV == 'production':
    UPDATED_DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    os.environ['UPDATED_DATABASE_URL'] = UPDATED_DATABASE_URL

    print(os.environ['UPDATED_DATABASE_URL'])

    # update_database_url()

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
        print('hit the root')

        return redirect(api.url_for(ApiResource))

    return app
