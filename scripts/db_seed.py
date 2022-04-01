import os
DATABASE_URL = os.environ['DATABASE_URL']
# UPDATED_DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

os.system('flask db upgrade')
os.system(f'psql {DATABASE_URL} -f /app/seed/countries.sql')
os.system(f'psql {DATABASE_URL} -f /app/seed/cities.sql')
