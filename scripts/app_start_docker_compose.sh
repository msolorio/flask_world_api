./scripts/db_apply_migrations.sh && ./scripts/db_seed.sh && waitress-serve --port=$PORT --call "run:create_app"
