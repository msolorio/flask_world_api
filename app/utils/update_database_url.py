import os

def update_database_url():
    print('calling helper function')

    FLASK_ENV = os.environ['FLASK_ENV']
    DATABASE_URL = os.environ['DATABASE_URL']
    
    # if FLASK_ENV == 'production':
    UPDATED_DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    os.environ['UPDATED_DATABASE_URL'] = UPDATED_DATABASE_URL

    print(os.environ['UPDATED_DATABASE_URL'])
