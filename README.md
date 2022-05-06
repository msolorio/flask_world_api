# World Data API
REST API for searching world data.

![world map](./readme-assets/world-map.jpg)

---

## Tech Used
- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Swagger / Open API UI

---

## Explore the API

Visit [`/api/docs`](https://world-data-api.herokuapp.com/api/docs) to explore Swagger UI or hit routes directly from a browser.

https://world-data-api.herokuapp.com/api/

---

## Routes

### Country
Countries by search term.<br>
`/api/countries/?search=<search-term>`

Countries by name.<br>
`/api/countries?name=<country-name>`

Countries by continent.<br>
`/api/countries?continent=<continent-name>`

Countries by government form.<br>
`/api/countries?governmentform=<government-form>`

Countries with population greater than / than...<br>
`/api/cities?population=gt:10000000`

Countries with life expectancy greater than / than...<br>
`/api/countries?lifeexpectancy=gt:80`

Countries with surface area greater than / than...<br>
`/api/countries?surfacearea=gt:1000000`

Return type
```json
{
  "_length": 0, // number of countries returned
  "countries": [] // array of country objects
}
```

---

### City
Cities by search term.<br>
`/api/cities/?search=<search-term>`

Cities within a given country.<br>
`/api/cities?country=<country-name>`

Capital city of a given country.<br>
`/api/cities?capitalof=<country-name>`

Cities by with population greater than / less than...<br>
`/api/cities?population=gt:1000000`

Return type
```json
{
  "_length": 0, // number of cities returned
  "cities": [] // array of city objects
}
```

---

### Future Features
Add a spoken language component to the API.

Countries that speak a given language.<br>
`/api/countries?language=<language>`

All languages spoken in a given country.<br>
`/api/languages?country=<country-name>`

All official languages spoken in a given country.<br>
`/api/languages?country=<country-name>&isofficial=true`

---