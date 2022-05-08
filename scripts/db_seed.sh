flask db upgrade

# Clear records
psql ${DATABASE_URL} -f /app/seed/clear_db.sql

# Adds records to db
psql ${DATABASE_URL} -f /app/seed/countries.sql
psql ${DATABASE_URL} -f /app/seed/cities.sql
