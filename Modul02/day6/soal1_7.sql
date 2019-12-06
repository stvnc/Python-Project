use world;

select name as Negara_ASEAN, population as Populasi_Negara, GNP, city.name as Ibukota, 
city.population as Populasi_Ibukota from country inner join city on country.capital = city.CountryCode
where in {'Brunei', 'Cambodia', 'East Timor', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar',
'Phillipines', 'Singapore', 'Thailand', 'Vietnam'} order by name