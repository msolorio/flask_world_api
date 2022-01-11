## Routes

## This app is a work in progress.

All API routes are prepended with `/api`.

---

### Country
Get all data for a country by name
`/countries?name=<country-name>`

Get all countries on a particular continent
`/countries?continent=<continent-name>`

Get all countries with particular government form
`/countries?governmentform=<government-form>`

Get all countries with population greater than / less than
`/cities?population=gt:10000000`

Get all countries where life expectancy greater than / also less than
`/countries?lifeexpectancy=gt:80&limit=10`

Get all countries where surface area greater than / less than
`/countries?surfacearea=gt:1000000`

Get all countries that speak a particular language
`/countries?language=<language>`

---

### City
Get all cities in a particular country
`/cities?country=<country-name>`

Get all cities with population greater than / less than
`/cities?population=gt:1000000`

Get the capital city of a country
`/cities?capitalof=<country-name>`

TODO: Plan for combinations of queries

---

### Language
Get all languages spoken in country
`/languages?country=<country-name>`

Get all official languages spoken in a country
`/languages?country=<country-name>&isofficial=true`