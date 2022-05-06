export FLASK_APP=run:app
export FLASK_ENV=development

pipenv shell

# Will add migrations folder to application.
# Contents of this folder need to be added to version control.
flask db init
