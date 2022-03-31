flask db upgrade

psql ${SQLALCHEMY_DATABASE_URI} -f /app/seed/countries.sql
psql ${SQLALCHEMY_DATABASE_URI} -f /app/seed/cities.sql
