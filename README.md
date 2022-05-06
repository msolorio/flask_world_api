## World Data API
REST API for searching world data.

https://world-data-api.herokuapp.com/api/

### Technologies
- Flask
- PostgreSQL
- SQLAlchemy
- Swagger / Open API UI
- And other players in the flask ecosystem

### Features

- Perform detailed queries for information about countries and cities around the world.
- Perform CRUD opperations on countries and cities.
- Visit Open API / Swagger UI documentation to explore API.

### [Explore the API](https://world-data-api.herokuapp.com/api/docs)

Visit [`/api/docs`](https://world-data-api.herokuapp.com/api/docs) to explore the Open API / Swagger UI documentation.
- shows available routes
- query country and city data

---

## Routes

---

### Country
Search countries by name.
`/api/countries?name=<country-name>`

Search countries by continent.
`/api/countries?continent=<continent-name>`

Search countries by government form.
`/api/countries?governmentform=<government-form>`

Search countries with population greater than / than...
`/api/cities?population=gt:10000000`

Search countries with life expectancy greater than / than...
`/api/countries?lifeexpectancy=gt:80`

Search countries with surface area greater than / than...
`/api/countries?surfacearea=gt:1000000`

---

### City
Search cities within a given country.
`/api/cities?country=<country-name>`

Find the capital city of a given country.
`/api/cities?capitalof=<country-name>`

Search cities by with population greater than / less than...
`/api/cities?population=gt:1000000`

---

### Future Features
I would like to add a spoken language component to the API.

Search cities that speak a given language.
`/api/countries?language=<language>`

Get all languages spoken in a given country.
`/api/languages?country=<country-name>`

Get all official languages spoken in a given country.
`/api/languages?country=<country-name>&isofficial=true`

---