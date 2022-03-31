flask db upgrade

psql ${DATABASE_URL} -f /app/seed/countries.sql
psql ${DATABASE_URL} -f /app/seed/cities.sql
