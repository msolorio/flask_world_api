flask db upgrade

psql ${UPDATED_DATABASE_URL} -f /app/seed/countries.sql
psql ${UPDATED_DATABASE_URL} -f /app/seed/cities.sql
