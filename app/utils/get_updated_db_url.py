import os

def get_updated_db_url():
    DATABASE_URL = os.environ['DATABASE_URL']
    return DATABASE_URL.replace('postgres://', 'postgresql://', 1)
