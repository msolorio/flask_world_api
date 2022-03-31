FROM python:3.9

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY . .

CMD ["waitress-serve", "--call", "run:create_app"]