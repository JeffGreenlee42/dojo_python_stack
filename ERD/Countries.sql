USE world;
select * from countries;
SELECT * from languages;
SELECT * from cities;

SELECT countries.name AS "Country", languages.language, languages.percentage AS "Language Percentage"  FROM countries 
JOIN languages ON countries.code = languages.country_code
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;