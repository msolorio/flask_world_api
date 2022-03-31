import os

def update_database_url():
    FLASK_ENV = os.environ['FLASK_ENV']
    DATABASE_URL = os.environ['DATABASE_URL']
    
    if FLASK_ENV == 'production':
        UPDATED_DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
        os.environ['DATABASE_URL'] = UPDATED_DATABASE_URL