import os
from ..app.utils.get_updated_db_url import get_updated_db_url
UPDATED_DATABASE_URL = get_updated_db_url()

os.system('flask db upgrade')
os.system(f'psql {UPDATED_DATABASE_URL} -f /app/seed/countries.sql')
os.system(f'psql {UPDATED_DATABASE_URL} -f /app/seed/cities.sql')
