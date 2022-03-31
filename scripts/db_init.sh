export FLASK_APP=run:app
export FLASK_ENV=development

pipenv shell

flask db init
