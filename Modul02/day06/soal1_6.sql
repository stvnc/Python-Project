use world;
select code as countryCode, name, language, isofficial, percentage from country inner join countryLanguage
on country.Code = countryLanguage.CountryCode where language = 'English'
order by percentage desc limit 10;
