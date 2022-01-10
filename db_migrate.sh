export FLASK_APP=run:app
export FLASK_ENV=development

pipenv shell

flask db migrate -m '$1'
flask db upgrade
