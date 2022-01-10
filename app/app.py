from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from .models import db, ma
from .api_bp import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)

    app.register_blueprint(api_bp,  url_prefix='/api')

    @app.route('/')
    def root():
        return redirect(url_for('api_bp.api_root'))

    return app
