./scripts/db_apply_migrations.sh

./scripts/db_seed.sh

flask run -p 5000 -h 0.0.0.0
