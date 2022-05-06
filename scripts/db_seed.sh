flask db upgrade

# Adds records to db
psql ${DATABASE_URL} -f /app/seed/countries.sql
psql ${DATABASE_URL} -f /app/seed/cities.sql
