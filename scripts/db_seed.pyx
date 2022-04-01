import os
DATABASE_URL = os.environ['DATABASE_URL']

os.system('flask db upgrade')
os.system(f'psql {DATABASE_URL} -f /app/seed/countries.sql')
os.system(f'psql {DATABASE_URL} -f /app/seed/cities.sql')
