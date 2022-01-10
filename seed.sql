\c world_db

INSERT INTO countries
(code, name, continent, region, surfacearea, indepyear, population, lifeexpectancy, gnp, gnpold, localname, governmentform, headofstate, capital_id, code2)
VALUES
('AFG', 'Afghanistan', 'Asia', 'Southern and Central Asia', 652090, 1919, 22720000, 45.900002, 5976.00, null, 'Afganistan/Afqanestan', 'Islamic Emirate', 'Mohammad Omar', 1, 'AF');

INSERT INTO cities
(id, name, countrycode, district, population)
VALUES
(1, 'Kabul', 'AFG', 'Kabol', 1780000),
(2, 'Qandahar', 'AFG', 'Qandahar', 237500),
(3, 'Herat', 'AFG', 'Herat', 186800),
(4, 'Mazar-e-Sharif', 'AFG', 'Balkh', 127800);
