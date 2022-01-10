export FLASK_APP=run:app
export FLASK_ENV=development

# activates pipenv venv in existing shell
. $(pipenv --venv)/bin/activate

flask run -h 0.0.0.0