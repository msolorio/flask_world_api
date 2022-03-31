FROM python:3.9

RUN pip install pipenv
ENV FLASK_ENV=development
ENV FLASK_APP=run:app
ENV DATABASE_URL=postgresql://postgres:postgres@worlddb:5432/world_db
ENV DEBUG=True

WORKDIR /app

RUN apt-get update
# TODO: troubleshoot installing v14 to match the DB installation
RUN apt-get -y install postgresql

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy


COPY . .

CMD ["waitress-serve", "--call", "run:create_app"]